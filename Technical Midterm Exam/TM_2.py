month_mapping = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December"
}

date_str = input("Please enter a date (mm/dd/yyyy format, use 0 for single digits): ")
month_part, day_part, year_part = date_str.split('/')

month_full_name = month_mapping[month_part]
formatted_date = f"{month_full_name} {int(day_part)}, {year_part}"

print("Formatted Date:", formatted_date)
