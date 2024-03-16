from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    talker_node = Node(
        package='basic_comms',
        executable='talker',
        output='screen'
    )

    listener_node = Node(
        package='basic_comms',
        executable='listener',
        output='screen'
    )

    rqt_graph_node = Node(
        package='rqt_graph',
        executable='rqt_graph',
        output='screen'
    )

    lsin_node = Node(
            package='basic_comms',
            executable='lsin',
            output='screen'
    )

    tsin_node = Node(
            package='basic_comms',
            executable='tsin',
            output='screen'
    )

    l_d = LaunchDescription([lsin_node, tsin_node])
    return l_d
