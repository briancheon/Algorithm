import requests
import subprocess
import os
import json
import time
import hashlib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# ─────────────────────────────────────────
#  STEP 1: Log in with Selenium to get cookie
# ─────────────────────────────────────────
def get_session_cookie():
    if not BOJ_ID or not BOJ_PASSWORD:
        print("❌ BOJ_ID or BOJ_PASSWORD environment variable not set")
        return None

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)

    try:
        print("🔐 Logging in to Baekjoon...")
        driver.get("https://www.acmicpc.net/login")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "login_user_id")))

        driver.find_element(By.ID, "login_user_id").send_keys(BOJ_ID)
        driver.find_element(By.ID, "login_password").send_keys(BOJ_PASSWORD)
        driver.find_element(By.ID, "submit_button").click()

        # Wait until redirected away from login page
        wait.until(EC.url_changes("https://www.acmicpc.net/login"))

        cookie = driver.get_cookie("OnlineJudge")
        if not cookie:
            print("❌ Login failed — please check your BOJ_ID and BOJ_PASSWORD secrets")
            return None

        print("✅ Login successful")
        return cookie["value"]

    except Exception as e:
        print(f"❌ Selenium error: {e}")
        return None

    finally:
        driver.quit()

# ─────────────────────────────────────────
#  STEP 2: Fetch all solved problems from solved.ac
# ─────────────────────────────────────────
def get_all_solved():
    print(f"📋 Fetching solved problems for {BOJ_ID}...")
    solved = []
    page = 1

    while True:
        url = (
            f"https://solved.ac/api/v3/search/problem"
            f"?query=solved_by:{BOJ_ID}&sort=id&direction=desc&page={page}"
        )
        resp = requests.get(url, headers={"Accept": "application/json"})

        if resp.status_code != 200:
            print(f"  ⚠️  solved.ac API error: {resp.status_code}")
            break

        data = resp.json()
        items = data.get("items", [])
        if not items:
            break

        solved.extend([item["problemId"] for item in items])

        if len(solved) >= data["count"]:
            break

        page += 1
        time.sleep(0.5)

    print(f"  Found {len(solved)} solved problems total")
    return solved

# ─────────────────────────────────────────
#  STEP 3: Fetch most recent accepted submission from Baekjoon
# ─────────────────────────────────────────
def get_accepted_submission(problem_id, session_cookie):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Cookie": f"OnlineJudge={session_cookie}"
    }

    # result_id=4 means "Accepted" — table sorted by date desc so first row = most recent
    url = f"https://www.acmicpc.net/status?user_id={BOJ_ID}&problem_id={problem_id}&result_id=4"
    resp = session.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")

    row = soup.select_one("table#status-table tbody tr")
    if not row:
        print(f"  ⚠️  No accepted submission found for problem {problem_id}")
        return None, None, None

    submission_id = row.select_one("td:first-child").text.strip()
    lang_cell     = row.select_one(".language")
    lang          = lang_cell.text.strip() if lang_cell else "unknown"

    source_url = f"https://www.acmicpc.net/source/{submission_id}"
    resp = session.get(source_url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")

    code_tag = soup.select_one("#source-code")
    if not code_tag:
        print(f"  ⚠️  Could not retrieve source for submission {submission_id}")
        return None, None, None

    return code_tag.text, lang, submission_id

# ─────────────────────────────────────────
#  STEP 4: Save file and git commit
# ─────────────────────────────────────────
def commit_solution(problem_id, code, lang, is_update=False):
    ext         = LANG_EXTENSIONS.get(lang, "txt")
    folder_name = LANG_FOLDERS.get(ext, f"baekjoon/{ext}")  # fallback for new languages
    folder      = os.path.join(REPO_PATH, "Algorithm", folder_name)

    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, f"{problem_id}.{ext}")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)

    commit_msg = f"Update Sol {problem_id}" if is_update else f"Sol {problem_id}"

    subprocess.run(["git", "add", filepath])
    subprocess.run(["git", "commit", "-m", commit_msg])
    print(f"  ✅ Committed: {commit_msg}  ({lang}  →  {filepath})")

# ─────────────────────────────────────────
#  HELPER: Hash code content to detect changes
# ─────────────────────────────────────────
def hash_code(code):
    return hashlib.md5(code.encode("utf-8")).hexdigest()

# ─────────────────────────────────────────
#  STATE — tracks each problem's submission_id and code hash
#
#  state.json format:
#  {
#    "problems": {
#      "1000": { "submission_id": "12345678", "hash": "abc123..." },
#      "1001": { "submission_id": "87654321", "hash": "def456..." }
#    }
#  }
# ─────────────────────────────────────────
def load_state():
    if os.path.exists("state.json"):
        with open("state.json") as f:
            data = json.load(f)
            # Migrate old format {"committed": [...]} to new format
            if "committed" in data:
                print("  🔄 Migrating state.json to new format...")
                return {"problems": {str(p): {} for p in data["committed"]}}
            return data
    return {"problems": {}}

def save_state(state):
    with open("state.json", "w") as f:
        json.dump(state, f, indent=2)

# ─────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────
def run():
    # 1. Login and get fresh cookie
    session_cookie = get_session_cookie()
    if not session_cookie:
        return

    # 2. Load state and fetch all solved problems
    state    = load_state()
    problems = state["problems"]

    all_solved = get_all_solved()

    new_count    = 0
    update_count = 0
    skip_count   = 0

    # 3. Process every solved problem
    for problem_id in all_solved:
        pid = str(problem_id)
        print(f"  Processing problem {problem_id}...")

        code, lang, submission_id = get_accepted_submission(problem_id, session_cookie)
        if not code:
            continue

        current_hash = hash_code(code)

        if pid not in problems:
            # ── Brand new problem ──────────────────────────
            commit_solution(problem_id, code, lang, is_update=False)
            problems[pid] = {"submission_id": submission_id, "hash": current_hash}
            new_count += 1

        elif problems[pid].get("hash") != current_hash:
            # ── Already committed but code has changed ─────
            commit_solution(problem_id, code, lang, is_update=True)
            problems[pid] = {"submission_id": submission_id, "hash": current_hash}
            update_count += 1

        else:
            # ── Identical to what's already in the repo ────
            skip_count += 1

        save_state(state)
        time.sleep(2)  # be polite to Baekjoon's servers

    print(f"\n📊 Summary: {new_count} new | {update_count} updated | {skip_count} unchanged")

    # 4. Push all commits at once
    subprocess.run(["git", "push"])
    print("🚀 All done! Solutions pushed to GitHub.")

if __name__ == "__main__":
    run()
