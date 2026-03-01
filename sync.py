import requests
import subprocess
import os
import json
import time
from bs4 import BeautifulSoup

# ─────────────────────────────────────────
#  CONFIG — all read from GitHub Secrets
# ─────────────────────────────────────────
BOJ_ID       = os.environ.get("BOJ_ID")
BOJ_PASSWORD = os.environ.get("BOJ_PASSWORD")
REPO_PATH    = "."

LANG_EXTENSIONS = {
    "C++17": "cpp", "C++14": "cpp", "C++20": "cpp", "C++23": "cpp",
    "C": "c", "C11": "c",
    "Java 11": "java", "Java 8": "java", "Java 21": "java",
    "Python 3": "py", "PyPy3": "py", "Python 2": "py",
    "Kotlin (JVM)": "kt",
    "Swift": "swift",
    "Go": "go",
    "Ruby": "rb",
    "Rust 2021": "rs",
}

LANG_FOLDERS = {
    "cpp": "baekjoon/cpp",
    "c":   "baekjoon/c",
    "py":  "baekjoon/python",
}

# Realistic browser headers to avoid 403
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
}

# ─────────────────────────────────────────
#  STEP 1: Log in with requests to get session
# ─────────────────────────────────────────
def get_session():
    if not BOJ_ID or not BOJ_PASSWORD:
        print("❌ BOJ_ID or BOJ_PASSWORD environment variable not set")
        return None

    session = requests.Session()

    print("🔐 Logging in to Baekjoon...")

    # Step 1: Load the login page to get CSRF token
    resp = session.get("https://www.acmicpc.net/login", headers=HEADERS)
    print(f"  Login page status: {resp.status_code}")

    if resp.status_code != 200:
        print(f"❌ Could not load login page (status {resp.status_code})")
        return None

    soup = BeautifulSoup(resp.text, "html.parser")
    csrf = soup.select_one("input[name=csrf_key]")

    if not csrf:
        print("  ⚠️  Could not find CSRF token — dumping page snippet for debug:")
        print(resp.text[:500])
        return None

    csrf_value = csrf["value"]
    print(f"  Found CSRF token: {csrf_value[:10]}...")

    # Small delay to mimic human behavior
    time.sleep(1)

    # Step 2: Submit login form
    login_data = {
        "login_user_id": BOJ_ID,
        "login_password": BOJ_PASSWORD,
        "csrf_key": csrf_value,
        "auto_login": "on"
    }

    login_headers = {
        **HEADERS,
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://www.acmicpc.net/login",
        "Origin": "https://www.acmicpc.net",
    }

    resp = session.post(
        "https://www.acmicpc.net/signin",
        data=login_data,
        headers=login_headers,
        allow_redirects=True
    )

    print(f"  Login POST status: {resp.status_code}, final URL: {resp.url}")

    # Step 3: Verify login succeeded
    if "OnlineJudge" not in session.cookies:
        print("❌ Login failed — OnlineJudge cookie not found after POST")
        # Check if we're still on the login page (wrong credentials)
        if "login" in resp.url:
            print("  Still on login page — check your BOJ_ID and BOJ_PASSWORD secrets")
        return None

    print("✅ Login successful")
    return session

# ─────────────────────────────────────────
#  STEP 2: Fetch all solved problems from solved.ac
#  Returns list of (problem_id, problem_name)
# ─────────────────────────────────────────
def get_all_solved():
    print(f"📋 Fetching solved problems for {BOJ_ID}...")
    solved = []
    page   = 1

    while True:
        url = (
            f"https://solved.ac/api/v3/search/problem"
            f"?query=solved_by:{BOJ_ID}&sort=id&direction=desc&page={page}"
        )
        resp = requests.get(url, headers={"Accept": "application/json"})

        if resp.status_code != 200:
            print(f"  ⚠️  solved.ac API error: {resp.status_code}")
            break

        data  = resp.json()
        items = data.get("items", [])
        if not items:
            break

        for item in items:
            problem_id   = item["problemId"]
            problem_name = item.get("titleKo") or item.get("titleEn", f"Problem {problem_id}")
            solved.append((problem_id, problem_name))

        if len(solved) >= data["count"]:
            break

        page += 1
        time.sleep(0.5)

    print(f"  Found {len(solved)} solved problems total")
    return solved

# ─────────────────────────────────────────
#  STEP 3: Fetch latest accepted submission from Baekjoon
#  Returns (submission_id, code, lang)
# ─────────────────────────────────────────
def get_accepted_submission(problem_id, session):
    # result_id=4 means "Accepted"
    url  = f"https://www.acmicpc.net/status?user_id={BOJ_ID}&problem_id={problem_id}&result_id=4"
    resp = session.get(url, headers=HEADERS)
    soup = BeautifulSoup(resp.text, "html.parser")

    print(f"    Submission page status: {resp.status_code}")

    row = soup.select_one("table#status-table tbody tr")
    if not row:
        print(f"  ⚠️  No accepted submission found for problem {problem_id}")
        print(f"    (Make sure your Baekjoon profile is set to public)")
        return None, None, None

    submission_id = row.select_one("td:first-child").text.strip()
    lang_cell     = row.select_one(".language")
    lang          = lang_cell.text.strip() if lang_cell else "unknown"

    print(f"    Found submission {submission_id} in {lang}")

    source_url = f"https://www.acmicpc.net/source/{submission_id}"
    resp       = session.get(source_url, headers=HEADERS)
    soup       = BeautifulSoup(resp.text, "html.parser")

    code_tag = soup.select_one("#source-code")
    if not code_tag:
        print(f"  ⚠️  Could not retrieve source for submission {submission_id}")
        return None, None, None

    return submission_id, code_tag.text, lang

# ─────────────────────────────────────────
#  STEP 4: Save file and git commit
# ─────────────────────────────────────────
def sanitize(name):
    """Remove characters that are invalid in filenames."""
    invalid = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for ch in invalid:
        name = name.replace(ch, "")
    return name.strip()

def commit_solution(problem_id, problem_name, code, lang, is_update=False):
    ext         = LANG_EXTENSIONS.get(lang, "txt")
    folder_name = LANG_FOLDERS.get(ext, f"baekjoon/{ext}")
    folder      = os.path.join(REPO_PATH, "Algorithm", folder_name)

    os.makedirs(folder, exist_ok=True)

    # Filename: "1000 (A+B).cpp"
    safe_name = sanitize(problem_name)
    filename  = f"{problem_id} ({safe_name}).{ext}"
    filepath  = os.path.join(folder, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)

    commit_message = f"Sol {problem_id} Updated" if is_update else f"Sol {problem_id}"

    result = subprocess.run(["git", "add", filepath], capture_output=True, text=True)
    print(f"    git add: {result.returncode} {result.stderr.strip()}")

    result = subprocess.run(["git", "commit", "-m", commit_message], capture_output=True, text=True)
    print(f"    git commit: {result.returncode} {result.stdout.strip()} {result.stderr.strip()}")

    print(f"  ✅ {'Updated' if is_update else 'Committed'}: {commit_message}  ({lang}  →  {filepath})")

# ─────────────────────────────────────────
#  STATE — track problem → latest submission ID
# ─────────────────────────────────────────
def load_state():
    if os.path.exists("state.json"):
        with open("state.json") as f:
            return json.load(f)
    return {}

def save_state(state):
    with open("state.json", "w") as f:
        json.dump(state, f, indent=2)

# ─────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────
def run():
    # 1. Login and get session
    session = get_session()
    if not session:
        return

    # 2. Load state and find all solved problems
    state      = load_state()
    all_solved = get_all_solved()

    new_problems      = [(pid, pname) for pid, pname in all_solved if str(pid) not in state]
    existing_problems = [(pid, pname) for pid, pname in all_solved if str(pid) in state]

    print(f"🆕 {len(new_problems)} new problem(s) to commit")
    print(f"🔍 Checking {len(existing_problems)} existing problem(s) for newer submissions\n")

    # 3. Commit new problems
    for problem_id, problem_name in new_problems:
        print(f"  Processing new problem {problem_id} ({problem_name})...")
        submission_id, code, lang = get_accepted_submission(problem_id, session)

        if not code:
            continue

        commit_solution(problem_id, problem_name, code, lang, is_update=False)
        state[str(problem_id)] = submission_id
        save_state(state)
        time.sleep(2)

    # 4. Check existing problems for newer submissions
    for problem_id, problem_name in existing_problems:
        print(f"  Checking problem {problem_id} ({problem_name}) for updates...")
        submission_id, code, lang = get_accepted_submission(problem_id, session)

        if not code:
            continue

        if submission_id != state[str(problem_id)]:
            print(f"  🔄 Newer submission found for problem {problem_id}!")
            commit_solution(problem_id, problem_name, code, lang, is_update=True)
            state[str(problem_id)] = submission_id
            save_state(state)

        time.sleep(2)

    # 5. Push all commits at once
    result = subprocess.run(["git", "push"], capture_output=True, text=True)
    print(f"  git push: {result.returncode} {result.stdout.strip()} {result.stderr.strip()}")
    print("\n🚀 All done! Solutions pushed to GitHub.")

if __name__ == "__main__":
    run()