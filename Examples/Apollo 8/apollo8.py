#Apollo 8 example
exec(compile(open("/Users/jago/Documents/Uni/Other/CV/N-Body-Simulator/mainV0_old.py", "rb").read(), "/Users/jago/Documents/Uni/Other/CV/N-Body-Simulator/mainV0_old.py", 'exec'))

apollo8 = Body("Apollo 8", 10000, 24429050.76, -23821493.926, 18554257.052, 3576.07, -2036.789, 528.589)
earth = Body("Earth", 5.97219e24, -2094283.364, 3845613.310, 353871.670, -11.888, -5.771, -0.398)
moon = Body("Moon", 734.9e20, 170266429.305, -312650550.581, 28769968.167, 966.524, 46.919, 32.350)

Body.simulate(0, 1000000, 1, 1000)

Body.output_all()