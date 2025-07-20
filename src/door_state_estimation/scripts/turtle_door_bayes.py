import rospy
from turtlesim.srv import Spawn, SetPen, TeleportAbsolute

def teleport_robot(robot_name, robot_x, robot_y):
    rospy.wait_for_service(f'/{robot_name}/teleport_absolute')
    try:
        teleport = rospy.ServiceProxy(f'/{robot_name}/teleport_absolute', TeleportAbsolute)
        teleport(robot_x, robot_y, 0)
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")

if __name__ == "__main__":
    rospy.init_node('teleport_robot_node')
    robot_name = rospy.get_param('~robot_name', 'turtle1')
    robot_x = rospy.get_param('~robot_x', 5.0)
    robot_y = rospy.get_param('~robot_y', 5.0)
    teleport_robot(robot_name, robot_x, robot_y)