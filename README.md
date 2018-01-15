# AI Vector Field Navigation - Will update with instructions within due time.


1) init class:

        nav = navigation.vectorFields(max_vector=15, max_theta=1.0(radians))

        
2) Update Attractor position:

        nav.attractor(att_range, att_angle)


3) Update Repulsor position:

        nav.repulsor(rep_range, rep_angle)
        
       
4) Get heading:
        
        vector, theta, [dt_x, dt_y] = nav.get_heading()
