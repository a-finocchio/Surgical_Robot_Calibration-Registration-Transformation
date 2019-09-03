README.txt

---------------environment descrpition-----------------------
All the programs are based on Python3
The library includes numpy 1.15, scipy 1.10


---------------how to use-----------------------
Runing Assignment2.py will automatically input dataset from a-j and return you the results into two files 
"NAME-OUR-OUTPUT1.TXT' Output file that give the P_em_dimple'NAME-OUR-OUTPUT2.TXT' Output file that give tip location with respect to the CT image"



--------------------------------------
           Main  Functions
--------------------------------------__init__.py# Initialize the environment				--------------------------------------		invtrans.py	
Input: F rigid transform matrix(4*4)	
Output: inv(F) inverse transform of F matrix(4*4)# Inverse of rigid body transformation,  from F to inv(F)					
--------------------------------------	point_cloud_registration.py	
Input: c1 c2 two 3D point clouds(n*3)	
Output: F rigid transform matrix(4*4)# Point cloud registration, compute the rigid transform matrix with two input poind clouds		--------------------------------------		pivot_calibration.py	
Input: NF n rigid transformations matrix(4*4*n)	
Output: P two translations in one array(6*1)# Pivot calibration, compute the two translations using n input transformations matrix		--------------------------------------		import_calibrate_data.py	
Input: a_string a string relates to the debug file such as 'a','b','c',etc 	
Output: C_exp, C_origin ground truth and measured point cloud matrix(3*3375)# Collect in calbody and calreading data file, return ground truth and measured point cloud data for distortion correction		
--------------------------------------
distortion_correction.py	
Input: C_exp, C_origin, C_warp, point cloud data, txt file,  order a value for polynomial order	
Output: C_dewarp dewarped point cloud matrix(3*3375)# Read in calbody and calreading data file, warped data, and polynomial order, calculate the distortion correction polynomial using the calbody and calreading file, using the obtained coefficient to dewarp the warped data		

--------------------------------------
test_distortion_correction.py	
Input: a_string a string relates to the debug file such as 'a','b','c',etc 	
Output: P_EM_dimple array(3*1)# Read in calbody and calreading data file, warped data, and polynomial order, calculate the P_EM_dimple matrix for debugging with the output1 data file		
		--------------------------------------		Assigment2.py
Input: 	/	
Output: "NAME-OUR-OUTPUT1.TXT' Output file that give the P_em_dimple'NAME-OUR-OUTPUT2.TXT' Output file that give tip location with respect to the CT image"# Automatically run all steps in the suggested procedure, mainly output the tip location with respect to the CT image in the file 'NAME-OUR-OUTPUT2.TXT' 		


--------------------------------------
--------------------------------------
Developer: 
Tianyu Song   tsong11@jhu.edu
Huixiang Li   lhuixia1@jhu.edu
 	