#! /usr/bin/python3
import math, sys, getopt

def main(argv):
	found_n=False
	circle=False
	try:
		opts, args = getopt.getopt(argv,"hn:c:",["numsegments=","circle="])
	except getopt.GetoptError:
	    print 'rubberbandgen.py -n <number of segments> [-c <closed circle or line>]'
	    sys.exit(2)
	for opt, arg in opts:
	    if opt == '-h':
	        print 'rubberbandgen.py -n <number of segments> [-c <closed circle or line>]'
	        sys.exit()
	    elif opt in ("-n", "--numsegments"):
	        n = int(arg)
	        found_n=True
	    elif opt in ("-c", "--circle"):
			circle = bool(arg)
	if not found_n:
	    print "-n was not given"
	    print 'rubberbandgen.py -n <number of segments> [-c <closed circle or line>]'
	    sys.exit(2)

	start="<?xml version='1.0'?>\n\
	<sdf version='1.6'>\n\
	  <model name='rubber_rope'>\n"

	end="    <static>0</static>\n\
	    <allow_auto_disable>1</allow_auto_disable>\n\
	    <plugin name=\"virtual_rubber_band\" filename=\"libcosima_gazebo_virtual_rubber_band.so\"/>\n\
	  </model>\n\
	</sdf>"

	segmentWJ = "<!-- SEGMENT -->\n\
	<joint name='JREF_S_H' type='revolute2'>\n\
	  <parent>LSPREV</parent>\n\
	  <child>LHPOST</child>\n\
	  <pose frame=''>0 0 0 0 -0 0</pose>\n\
	  <axis>\n\
	    <xyz>1 0 0</xyz>\n\
	    <use_parent_model_frame>0</use_parent_model_frame>\n\
	    <limit>\n\
	      <lower>-0.0523599</lower>\n\
	      <upper>0.0523599</upper>\n\
	      <effort>-1</effort>\n\
	      <velocity>-1</velocity>\n\
	    </limit>\n\
	    <dynamics>\n\
	      <spring_reference>0</spring_reference>\n\
	      <spring_stiffness>0.1</spring_stiffness>\n\
	      <damping>0</damping>\n\
	      <friction>0</friction>\n\
	    </dynamics>\n\
	  </axis>\n\
	  <axis2>\n\
	    <xyz>0 0 1</xyz>\n\
	    <use_parent_model_frame>0</use_parent_model_frame>\n\
	    <dynamics>\n\
	      <spring_reference>0</spring_reference>\n\
	      <spring_stiffness>0.1</spring_stiffness>\n\
	      <damping>0.01</damping>\n\
	      <friction>0</friction>\n\
	    </dynamics>\n\
	    <limit>\n\
	      <lower>-0.06</lower>\n\
	      <upper>0.06</upper>\n\
	      <effort>-1</effort>\n\
	      <velocity>-1</velocity>\n\
	    </limit>\n\
	  </axis2>\n\
	  <physics>\n\
	    <provide_feedback>true</provide_feedback>\n\
	    <ode>\n\
	      <implicit_spring_damper>true</implicit_spring_damper>\n\
	      <cfm_damping>true</cfm_damping>\n\
	      <limit>\n\
	        <cfm>0.01</cfm>\n\
	        <erp>0.2</erp>\n\
	      </limit>\n\
	      <suspension>\n\
	        <cfm>0.01</cfm>\n\
	        <erp>0.2</erp>\n\
	      </suspension>\n\
	    </ode>\n\
	  </physics>\n\
	</joint>\n"

	segmentWOJ = "<!-- SEGMENT -->\n\
	<link name='LHPOST'>\n\
	  <gravity>false</gravity>\n\
	  <pose frame=''>LHX LHY -0 0 -0 LHRZ</pose>\n\
	  <inertial>\n\
	    <mass>0.0001</mass>\n\
	    <inertia>\n\
	      <ixx>4e-11</ixx>\n\
	      <ixy>0</ixy>\n\
	      <ixz>0</ixz>\n\
	      <iyy>4e-11</iyy>\n\
	      <iyz>0</iyz>\n\
	      <izz>4e-11</izz>\n\
	    </inertia>\n\
	    <pose frame=''>0 0 0 0 -0 0</pose>\n\
	  </inertial>\n\
	  <self_collide>0</self_collide>\n\
	  <kinematic>0</kinematic>\n\
	  <!--visual name='visual'>\n\
	    <pose frame=''>0 0 0 0 -0 0</pose>\n\
	    <geometry>\n\
	      <sphere>\n\
	        <radius>0.001</radius>\n\
	      </sphere>\n\
	    </geometry>\n\
	    <material>\n\
	      <lighting>1</lighting>\n\
	      <script>\n\
	        <uri>file://media/materials/scripts/gazebo.material</uri>\n\
	        <name>Gazebo/Grey</name>\n\
	      </script>\n\
	      <shader type='pixel'>\n\
	        <normal_map>__default__</normal_map>\n\
	      </shader>\n\
	      <ambient>0.3 0.3 0.3 1</ambient>\n\
	      <diffuse>0.7 0.7 0.7 1</diffuse>\n\
	      <specular>0.01 0.01 0.01 1</specular>\n\
	      <emissive>0 0 0 1</emissive>\n\
	    </material>\n\
	    <transparency>0</transparency>\n\
	    <cast_shadows>1</cast_shadows>\n\
	  </visual-->\n\
	</link>\n\
	<joint name='JPRI_S_H' type='prismatic'>\n\
	  <parent>LHPOST</parent>\n\
	  <child>LSPOST</child>\n\
	  <pose frame=''>0 0 0 0 -0 0</pose>\n\
	  <axis>\n\
	    <xyz>0 1 0</xyz>\n\
	    <use_parent_model_frame>0</use_parent_model_frame>\n\
	    <limit>\n\
	      <lower>0</lower>\n\
	      <upper>0.05</upper>\n\
	      <effort>-1</effort>\n\
	      <velocity>-1</velocity>\n\
	    </limit>\n\
	    <dynamics>\n\
	      <spring_reference>0</spring_reference>\n\
	      <spring_stiffness>12.0</spring_stiffness>\n\
	      <damping>4.0</damping>\n\
	      <friction>0</friction>\n\
	    </dynamics>\n\
	  </axis>\n\
	  <physics>\n\
	    <provide_feedback>true</provide_feedback>\n\
	    <ode>\n\
	      <implicit_spring_damper>true</implicit_spring_damper>\n\
	      <limit>\n\
	        <cfm>0</cfm>\n\
	        <erp>0.2</erp>\n\
	      </limit>\n\
	      <suspension>\n\
	        <cfm>0</cfm>\n\
	        <erp>0.2</erp>\n\
	      </suspension>\n\
	    </ode>\n\
	  </physics>\n\
	</joint>\n\
	<link name='LSPOST'>\n\
	  <pose frame=''>LSX LSY -0 0 -0 LSRZ</pose>\n\
	  <inertial>\n\
	    <mass>0.0001</mass>\n\
	    <inertia>\n\
	      <ixx>2.9e-09</ixx>\n\
	      <ixy>0</ixy>\n\
	      <ixz>0</ixz>\n\
	      <iyy>1.1e-09</iyy>\n\
	      <iyz>0</iyz>\n\
	      <izz>1.9e-09</izz>\n\
	    </inertia>\n\
	    <pose frame=''>0 0 0 0 -0 0</pose>\n\
	  </inertial>\n\
	  <self_collide>1</self_collide>\n\
	  <kinematic>0</kinematic>\n\
	  <visual name='visual'>\n\
	    <pose frame=''>0 0 0 0 -0 0</pose>\n\
	    <geometry>\n\
	      <box>\n\
	        <size>0.002 0.015 0.01</size>\n\
	      </box>\n\
	    </geometry>\n\
	    <material>\n\
	      <lighting>1</lighting>\n\
	      <script>\n\
	        <uri>file://media/materials/scripts/gazebo.material</uri>\n\
	        <name>Gazebo/Orange</name>\n\
	      </script>\n\
	      <!--shader type='pixel'>\n\
	        <normal_map>__default__</normal_map>\n\
	      </shader>\n\
	      <ambient>0.3 0.3 0.3 1</ambient>\n\
	      <diffuse>0.7 0.7 0.7 1</diffuse>\n\
	      <specular>0.01 0.01 0.01 1</specular>\n\
	      <emissive>0 0 0 1</emissive-->\n\
	    </material>\n\
	    <transparency>0</transparency>\n\
	    <cast_shadows>1</cast_shadows>\n\
	  </visual>\n\
	  <collision name='collision'>\n\
	    <laser_retro>0</laser_retro>\n\
	    <max_contacts>10</max_contacts>\n\
	    <pose frame=''>0 0 0 0 -0 0</pose>\n\
	    <geometry>\n\
	      <box>\n\
	        <size>0.002 0.015 0.01</size>\n\
	      </box>\n\
	    </geometry>\n\
	    <surface>\n\
	      <friction>\n\
	        <ode>\n\
	          <mu>2</mu>\n\
	          <mu2>2</mu2>\n\
	          <fdir1>0 0 0</fdir1>\n\
	          <slip1>0</slip1>\n\
	          <slip2>0</slip2>\n\
	        </ode>\n\
	        <torsional>\n\
	          <coefficient>1</coefficient>\n\
	          <patch_radius>0</patch_radius>\n\
	          <surface_radius>0</surface_radius>\n\
	          <use_patch_radius>1</use_patch_radius>\n\
	          <ode>\n\
	            <slip>0</slip>\n\
	          </ode>\n\
	        </torsional>\n\
	      </friction>\n\
	      <bounce>\n\
	        <restitution_coefficient>0</restitution_coefficient>\n\
	        <threshold>1e+06</threshold>\n\
	      </bounce>\n\
	      <contact>\n\
	        <collide_without_contact>0</collide_without_contact>\n\
	        <collide_without_contact_bitmask>1</collide_without_contact_bitmask>\n\
	        <collide_bitmask>1</collide_bitmask>\n\
	        <ode>\n\
	          <soft_cfm>0</soft_cfm>\n\
	          <soft_erp>0.2</soft_erp>\n\
	          <kp>1e+13</kp>\n\
	          <kd>1</kd>\n\
	          <max_vel>0.01</max_vel>\n\
	          <min_depth>0</min_depth>\n\
	        </ode>\n\
	        <bullet>\n\
	          <split_impulse>1</split_impulse>\n\
	          <split_impulse_penetration_threshold>-0.01</split_impulse_penetration_threshold>\n\
	          <soft_cfm>0</soft_cfm>\n\
	          <soft_erp>0.2</soft_erp>\n\
	          <kp>1e+13</kp>\n\
	          <kd>1</kd>\n\
	        </bullet>\n\
	      </contact>\n\
	    </surface>\n\
	  </collision>\n\
	</link>\n"

	width=0.015
	c=width
	R=c/(2*math.sin(math.pi/n))
	theta=2*math.asin(c/(2*R))

	allSegment = ""
	for i in range(0, n):
		segment = ""
		if (i > 0):
			segment = segmentWJ + segmentWOJ
			segment = segment.replace("JREF_S_H", "joint_rev_s" + str(i-1) + "_h" + str(i))
			segment = segment.replace("LSPREV", "link_segment_" + str(i-1))
		else:
			segment = segmentWOJ

		hookPx=0
		hookPy=i*0.016
		segmentPx=0
		segmentPy = hookPy+0.0075
		segmentRz=0

		if circle:
			angle=theta*i
			segmentPx=R*math.cos(angle)
			segmentPy=R*math.sin(angle)
			# segmentPz=0
			segmentRz=angle

			distOfHook=-0.0075
			tx=-segmentPy
			ty=segmentPx
			norm = math.sqrt((tx * tx) + (ty * ty))
			hookPx = segmentPx + (tx * distOfHook / norm)
			hookPy = segmentPy + (ty * distOfHook / norm)

		segment = segment.replace("LHX", str(hookPx))
		segment = segment.replace("LHY", str(hookPy))
		segment = segment.replace("LHRZ", str(segmentRz))

		segment = segment.replace("LSX", str(segmentPx))
		segment = segment.replace("LSY", str(segmentPy))
		segment = segment.replace("LSRZ", str(segmentRz))

		# print("i: " + str(i) + ", angle: " + str(angle) + ", segmentPx: " + str(segmentPx) + ", segmentPy: " + str(segmentPy) + ", hookPx: " + str(hookPx) + ", hookPy: " + str(hookPy))
		
		segment = segment.replace("SEGMENT", "SEGMENT " + str(i))
		segment = segment.replace("LHPOST", "link_hook_" + str(i))
		segment = segment.replace("LSPOST", "link_segment_" + str(i))
		segment = segment.replace("JPRI_S_H", "joint_pri_s" + str(i) + "_h" + str(i))

		allSegment = allSegment + segment

	if circle:
		lastJoint=segmentWJ
		lastJoint=lastJoint.replace("JREF_S_H", "joint_rev_s" + str(n-1) + "_h" + str(0))
		lastJoint=lastJoint.replace("LSPREV", "link_segment_" + str(n-1))
		lastJoint=lastJoint.replace("LHPOST", "link_hook_" + str(0))
		allSegment=allSegment+lastJoint

	allSegment = start + allSegment + end

	print(allSegment)

if __name__ == "__main__":
   main(sys.argv[1:])