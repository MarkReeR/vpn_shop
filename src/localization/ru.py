# Misc buttons
no_permission = "У вас нет прав для выполнения данной команды!"
unknown_command = "Не могу понять команду :("
nice_try = "Nice try!"
select = {"select": "Выбрать"}
go_back = {"start": "⬅️ Назад"}

# main menu
def start_text(full_name):
    return f"Приветствую, {full_name}!\nТы можешь использовать:\n1) /cart чтобы ознакомиться с нашим товаром.\n2) /how_to_use для того чтобы узнать, как установить VPN\n3) /support чтобы связаться с нами."
start_buttons = {
    "cart": "🛒 Корзина",
    "how_to_use": "ℹ️ Инструкция по установке",
    "support": "☎ Меню тех. поддержки"  
}   

# cart menu
cart_info_text = "В разработек"
cart_buttons ={
    "start": "⬅️ Назад"
}

# help menu - Installation instructions
how_to_use = f"""
1️⃣ Скачиваем клиент <a href='https://www.wireguard.com/'>Wireguard</a>:

📱 Android: [<a href='https://play.google.com/store/apps/details?id=com.wireguard.android'>PlayStore</a>] [<a href='https://f-droid.org/repo/com.wireguard.android_491.apk'>F-Droid</a>]

📱 iOS: [<a href='https://itunes.apple.com/us/app/wireguard/id1451685025?ls=1&mt=12'>AppStore</a>]

💻 Windows: [<a href='https://download.wireguard.com/windows-client/wireguard-installer.exe'>С официального сайта</a>]

💻 Linux: [<a href='https://www.wireguard.com/install/'>На сайте</a>]

2️⃣ Покупаем подключение, скачиваем файл для подключения

3️⃣ Открываем приложение и добавляем скачанный файл

"""
help_buttons = {
    "telephone": "📱 телефон",
    "computer": "💻 ПК",
    "start": "⬅️ Назад"
}

# support menu
support_info_text = "В разработек\nhttps://youtu.be/dQw4w9WgXcQ?si=Ug5KS8ekxJiV3-le"
support_buttons = {
    "start": "⬅️ Назад"
}
