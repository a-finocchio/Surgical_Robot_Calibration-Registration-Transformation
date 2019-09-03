README.txt

---------------environment descrpition-----------------------
All the programs are based on Python3
The library includes numpy 1.15, scipy 1.10


---------------how to use-----------------------
Running ProgrammingAssigment3.py will automatically input dataset from a-j and return you the results in the ./OUTPUT/*.txt files 


--------------------------------------
           Main  Functions
--------------------------------------ProgrammingAssignment3.py
Input:	/	
Output: ./OUTPUT/*.txt# automatically import input files in the data directory and output results for PA3 as *.txt files for each test set 					--------------------------------------		ReadInput.py
Input:	/	
Output: /# Define ReadData(),  ReadData1(),  ReadMesh() functions							
--------------------------------------	ReadData()
Input: filename  *SampleReadingsTest.txt in the data directory	
Output: NS the sum of points recorded in A,B,D frames, Nsamps number of sample frames, data point cloud data in the frames# Read in 'PA3-**-SampleReadingsTest.txt' file in the data directory, return Ns, Nsamps, and data point clouds		

		--------------------------------------		ReadData1()
Input:	filename  *Problem3-Body*.txt in the data directory	
Output: N number of markers, a xyz coordinates of marker LEDs in body coordinates, tip xyz coordinates of tip in body coordinates# Read in '**Problem3-Body*.txt' file in the data directory, return N, number of markers, and xyz coordinates for a & tip 		

	--------------------------------------		ReadMesh()
Input:	filename Problem3MeshFile.sur in the data directory	
Output: Nv number of vertices, v xyz coordinates of vertices in CT coordinates, Nt number of triangles, tri vertex indices of the three vertices for each triangle# Read in '*Problem3MeshFile.sur' file in the data directory, return number of vertices and number of triangles, xyz coordinates for the vertices in CT coordinates, vertex indices of the three vertices for each triangle 		

	
--------------------------------------
ProjectionOnSegment.py
Input: c,p,q three points of the triangle	
Output: c_s projection on segment c*# apply the given three inputs to calculate the projection on segment c*			

--------------------------------------
FindClosestPoint.py	
Input: a, tri vertex indices of the three vertices for each triangle	
Output: c the closest point calculated# Find the closest point with a given triangle 		
	
		--------------------------------------		BoundingSphere.py
Input: v xyz coordinates of vertices in CT coordinates(N*3 matrix), tri vertex indices of the three vertices for each triangle(M*3 matrix)	
Output: qq center of the sphere(M*3 matrix), rr radius of the sphere(M*1 matrix)# Calculate the bounding sphere of the given triangle			


--------------------------------------
ErrorAnalysis.py
Input: /
Output: ./error_analysis/*.txt
# Automatically import results from the ProgrammingAssignment3.py and calculate the error between the debug files


--------------------------------------
--------------------------------------
Developer: 
Tianyu Song   tsong11@jhu.edu
Huixiang Li   lhuixia1@jhu.edu
 	