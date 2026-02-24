import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # استخدمي العمود الجاهز start_time_dt
    df["start_time_dt"] = pd.to_datetime(df["start_time_dt"], errors="coerce")

    # احذفي القيم الفاضية لو فيه
    df = df.dropna(subset=["start_time_dt"])

    # اعملي weekday منه
    df["weekday"] = df["start_time_dt"].dt.day_name()

    # ترتيب الأيام صح
    df["weekday_num"] = df["start_time_dt"].dt.weekday
    df = df.sort_values("weekday_num")

    return df