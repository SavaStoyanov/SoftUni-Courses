month = input()
nights = int(input())
ap_price = 0
st_price = 0


if month == 'May' or month == 'October':
    st_price = 50 * nights
    ap_price = 65 * nights
elif month == 'June' or month == 'September':
    st_price = 75.20 * nights
    ap_price = 68.70 * nights
elif month == 'July' or month == 'August':
    st_price = 76 * nights
    ap_price = 77 * nights

if nights > 7 and (month == 'May' or month == 'October'):
    st_price = st_price * 0.95
elif nights > 14:
    if month == 'May' or month == 'October':
        st_price = st_price * 0.70
    elif month == 'June' or month == 'September':
        st_price = st_price * 0.80
    else:
        ap_price = ap_price * 0.90

print(f"Apartment: {ap_price:.2f} lv.")
print(f"Studio: {st_price:.2f} lv.")
