from datetime import date

d_today = date.today()
new_year_day = date(d_today.year + 1,1,1)
diff_date = new_year_day - d_today

print(f'今年は後{diff_date.days}日')