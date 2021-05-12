import os
# 路径属性
# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = os.path.join(BASE_DIR, 'data')

# package = "com.painting.xswl"   #涂色
# package = "com.joypuzzle.xswl"   #拼图
# package = "com.defend.icebox"   #冰箱
# package = "com.difference.xswl"   #我找的贼快
package = "com.guess.video"   #猜猜这是谁

name = ["点点涂色", "我拼图贼6", "冰箱保卫战", "我找的贼快"]

# device_id = "2a60f2d9"
# device_id = "LE67A06340120555"

# device_id = "2a60f2d9"
# device_id = "G64HMROBNZUCIV79"
device_id = "GDBNW19809004953"


launchable_activity = "com.guess.video/com.liquid.box.WelcomeActivity"


