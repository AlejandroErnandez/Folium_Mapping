def icon_color(vlk_hight):
    if vlk_hight < 1500:
        return 'green'
    elif 1500 <= vlk_hight < 3000:
        return 'orange'
    else:
        return 'red'
