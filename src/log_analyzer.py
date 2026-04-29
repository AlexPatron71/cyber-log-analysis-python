import pandas as pd

LOG_FILE = "../data/sample_logs.csv"
OUTPUT_FILE = "../outputs/report.csv"


def load_logs():
    df = pd.read_csv(LOG_FILE)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


def detect_failed_logins(df):
    failed = df[(df["status_code"] == 401) & (df["endpoint"] == "/login")]
    return failed.groupby("ip").size().reset_index(name="failed_login_count")


def detect_bruteforce(failed_df, threshold=3):
    return failed_df[failed_df["failed_login_count"] >= threshold]


def top_ips(df):
    return df["ip"].value_counts().reset_index()
    # columns fix
    .rename(columns={"index": "ip", "ip": "count"})


def suspicious_endpoints(df):
    return df.groupby("endpoint").size().reset_index(name="hits").sort_values("hits", ascending=False)


def build_report(df):
    failed = detect_failed_logins(df)
    brute = detect_bruteforce(failed)
    endpoints = suspicious_endpoints(df)
    ips = top_ips(df)

    return {
        "failed_logins": failed,
        "bruteforce": brute,
        "top_ips": ips,
        "endpoints": endpoints
    }


def save_report(report):
    with pd.ExcelWriter("../outputs/report.xlsx") as writer:
        for name, data in report.items():
            data.to_excel(writer, sheet_name=name, index=False)


def main():
    df = load_logs()
    report = build_report(df)
    save_report(report)
    print("Report generated -> outputs/report.xlsx")


if __name__ == "__main__":
    main()
