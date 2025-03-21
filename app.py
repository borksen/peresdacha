from flask import Flask, render_template
from vk_user_info import get_vk_user_info  
import config

app = Flask(__name__)

STUDENT_DATA = {
    "name": config.NAME,
    "surname": config.SURNAME,
    "achievements": config.ACHIEVEMENTS,
}

vk_data = get_vk_user_info(config.VK_USER_ID, config.VK_ACCESS_TOKEN)

@app.route("/")
def resume():
    return render_template("resume.html", student=STUDENT_DATA, vk_data=vk_data)

@app.route("/refresh")
def refresh_resume():
    global vk_data
    vk_data = get_vk_user_info(config.VK_USER_ID, config.VK_ACCESS_TOKEN)
    return render_template("resume.html", student=STUDENT_DATA, vk_data=vk_data)

if __name__ == "__main__":
    app.run(debug=True)
