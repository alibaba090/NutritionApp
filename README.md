# NutritionApp
AWS System app service name:
Created symlink /etc/systemd/system/multi-user.target.wants/nutrition_app.service → /etc/systemd/system/nutrition_app.service.
To Open the properties file: sudo nano /etc/systemd/system/nutrition_app.service

Start the sysmd app:
$ sudo systemctl start your_app_name
$ sudo systemctl enable your_app_name

Stop the app:
sudo systemctl stop your_app_name
