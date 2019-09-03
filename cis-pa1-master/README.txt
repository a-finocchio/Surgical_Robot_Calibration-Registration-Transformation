README.txt

---------------environment descrpition-----------------------
All the programs are based on Python3
The packages include python.numpy , python.sys , and python.math


---------------how to use-----------------------
Please run Q4.py Q5.py and Q6.py to check the result



--------------------------------------
              Functions
--------------------------------------__init__.py# Initialize the environment		--------------------------------------		angle_2_rot.py
input:R_angle angle array(3*1 or 1*3) in rad	
output:R_rot rotation matrix(3*3)# Generate the rotation matrix from angle matrix using left multiplication		--------------------------------------		rot_2_angle.py	
Input: R_rot rotation matrix(3*3)	
Output: R_angle angle array(3*1 or 1*3) in rad# Generate the  angle matrix  from rotation matrix 		--------------------------------------		F_homo_multiple.py	
Input: F1 F2 rigid transform matrix (4*4)	
Output: F3 result rigid transform matrix (4*4)# Generate the rigid body transformation matrix between two homogenous 4*4  matrixes		--------------------------------------		F_Rp_multiple.py	
Input: R1 R2 rotation matrix(3*3), p1 p2 translation matrix(3*1)	
Output: F3 result rigid transform matrix (4*4)# Generate the rigid body transformation matrix between two rotation matrix and translation matrixes		--------------------------------------		invtrans.py	
Input: F rigid transform matrix(4*4)	
Output: inv(F) inverse transform of F matrix(4*4)# Inverse of rigid body transformation,  from F to inv(F)			
--------------------------------------	rot.py	
Input: angle_value angle in rad	
Output: Rot a rotation matrix(3*3) around specific xyz axis# Generate rotation matrix for specific xyz axis 		--------------------------------------		trans.py	
Input: R rotation matrix(3*3) and p translation (3*1)	
Output: F rigid body transformation matrix(4*4)# Generate the rigid body transformation matrix from rotation matrix and translation matrix using homogeneous representation		--------------------------------------		trans_angle.py	
Input: angle array(1*3) and p translation (3*1)	
Output: F rigid body transformation matrix(4*4)# Generate the rigid body transformation matrix from angle array and translation matrix using homogeneous representation		--------------------------------------		skew_build.py	
Input: x array(3*1 or 1*3)	
Output: skew(x) skew matrix(3*3)# Build up a 3*3 skew matrix with an array(3*1 or 1*3)			
--------------------------------------	point_cloud_registration.py	
Input: c1 c2 two 3D point clouds(n*3)	
Output: F rigid transform matrix(4*4)# Point cloud registration, compute the rigid transform matrix with two input poind clouds		--------------------------------------		pivot_calibration.py	
Input: NF n rigid transformations matrix(4*4*n)	
Output: P two translations in one array(6*1)# Pivot calibration, compute the two translations using n input transformations matrix		--------------------------------------		Q4.py
Input: Provided files in the PA data folder
Output: C_expected, F_D, F_A the calculated results
# Read in the data from the provided folder, and calculate C_i_expected and F_D

--------------------------------------
Q5.py
Input: Provided files in the PA data folder
Output: P_EM_dimple 
# Read in the data from the provided folder, and calculate P_dimple

--------------------------------------
Q6.py
Input: Provided files in the PA data folder
Output: P_opt_dimple
# Read in the data from the provided folder to perform a pivot calibration of the optical tracking probe
		--------------------------------------		test_point_cloud_registration.py	
Input: num_rounds a value for automatic test times 	
Output: residual total residual value# implement an automatic test for point_cloud_registration.py, return total residual error between calculated F_c and the generated F_g		--------------------------------------		test_angle_rot.py	
Input: num_rounds a value for automatic test times 	
Output: residual total residual value# implement an automatic test for angle_2_rot.py and rot_2_angle, return total residual error between calculated angle and the generated angle	




--------------------------------------
--------------------------------------
Developer: 
Tianyu Song   tsong11@jhu.edu
Huixiang Li   lhuixia1@jhu.edu
 	