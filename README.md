# AI Vector Field Navigation - Will update with instructions within due time.

https://latex.codecogs.com/gif.latex?U%28q%29%3D%20U_A%28q%29%20&plus;%20U_R%28q%29s

1) init class:

        nav = navigation.vectorFields(max_vector=15, max_theta=1.0(radians))

        
2) Update Attractor position:

        nav.attractor(att_range, att_angle)


3) Update Repulsor position:

        nav.repulsor(rep_range, rep_angle)
        
       
4) Get heading:
        
        vector, theta, [dt_x, dt_y] = nav.get_heading()
