README.txt

---------------environment descrpition-----------------------
All the programs are based on Python3
The library includes numpy(version >= 1.15)


---------------how to use-----------------------
Running ProgrammingAssigment4.py will automatically input dataset from a-j and return you the results in the ./OUTPUT/*.txt files 


--------------------------------------
           Main  Functions
--------------------------------------ProgrammingAssignment4.py
Input:	/	
Output: ./OUTPUT/*.txt# automatically import input files in the data directory and output results for PA4 as *.txt files for each test set 					--------------------------------------	
tryICP.py	
Input: Nsample, number of samples; d, calculated point could of the tip; spheres, a list of class; octree, object;
Output: s,c the point calculated# iterate ice algorithm to find F_reg and return s = F_reg * d, and c. 		
	
		--------------------------------------	
FindClosestPoint.py	
Input: a, tri vertex indices of the three vertices for each triangle	
Output: c the closest point calculated# Find the closest point with a given triangle 		
	
		--------------------------------------	
FindClosestPoint.py	
Input: a, tri vertex indices of the three vertices for each triangle	
Output: c the closest point calculated# Find the closest point with a given triangle 		
	
		--------------------------------------		ReadInput.py
Input:	/	
Output: /# Define ReadData(),  ReadData1(),  ReadMesh() functions								
--------------------------------------
ProjectionOnSegment.py
Input: c,p,q three points of the triangle	
Output: c_s projection on segment c*# apply the given three inputs to calculate the projection on segment c*			

--------------------------------------	BoundingSphere.py
Input: v xyz coordinates of vertices in CT coordinates(N*3 matrix), tri vertex indices of the three vertices for each triangle(M*3 matrix)	
Output: qq center of the sphere(M*3 matrix), rr radius of the sphere(M*1 matrix)# Calculate the bounding sphere of the given triangle			


--------------------------------------
--------------------------------------
Developer: 
Tianyu Song   tsong11@jhu.edu
Huixiang Li   lhuixia1@jhu.edu
 	