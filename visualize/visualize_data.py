from load_data.load_data import load_data
import pandas as pd


df = load_data()

print("=" * 60)
print(" FIRST 5 ROWS")
print("=" * 60)
print(df.head())

# ── 2. Last Rows ──────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print(" LAST 5 ROWS")
print("=" * 60)
print(df.tail())

# ── 3. Shape ──────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print(" DATASET SHAPE")
print("=" * 60)
print(f"  Rows    : {df.shape[0]:,}")
print(f"  Columns : {df.shape[1]}")

# ── 4. Info ───────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print(" COLUMN TYPES & MEMORY USAGE")
print("=" * 60)
df.info()

# ── 5. Statistics ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print(" DESCRIPTIVE STATISTICS")
print("=" * 60)
print(df.describe())
print("=" * 60)
print(df['Class'].value_counts())

# ── 6. Missing Values ─────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print(" MISSING VALUES PER COLUMN")
print("=" * 60)
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_df = pd.DataFrame({"Missing": missing, "Percentage": missing_pct})
missing_df = missing_df[missing_df["Missing"] > 0]
if missing_df.empty:
    print(" No missing values found.")
else:
    print(missing_df)

# ── 7. Duplicates ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print(" DUPLICATE ROWS")
print("=" * 60)
dupes = df.duplicated().sum()
if dupes == 0:
    print(" No duplicate rows found.")
else:
    print(f" Found {dupes:,} duplicate rows ({dupes / len(df) * 100:.2f}%)")

print("\n" + "=" * 60)
print(" END OF EXPLORATORY DATA ANALYSIS")
print("=" * 60)