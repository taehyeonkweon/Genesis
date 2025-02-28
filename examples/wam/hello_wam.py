import genesis as gs

#gs.init(backend=gs.cpu)
gs.init(backend=gs.gpu)

scene = gs.Scene()

plane = scene.add_entity(
    gs.morphs.Plane(),
)

""" wam_arm = scene.add_entity(
    gs.morphs.MJCF(
        file = 'urdf/wam_descriptionpackage.xml',
        pos   = (0, 0, 0),
        euler = (0, 0, 90), # we follow scipy's extrinsic x-y-z rotation convention, in degrees,
        # quat  = (1.0, 0.0, 0.0, 0.0), # we use w-x-y-z convention for quaternions,
        scale = 1.0,
    ),
) """

wam_arm = scene.add_entity(
    gs.morphs.URDF(
        file = 'urdf/wam_description/urdf/wam.urdf',
        fixed = True,
    )
)

""" franka = scene.add_entity(
    gs.morphs.MJCF(
        file  = 'xml/franka_emika_panda/panda.xml',
        pos   = (0, 0, 0),
        euler = (0, 0, 90), # we follow scipy's extrinsic x-y-z rotation convention, in degrees,
        # quat  = (1.0, 0.0, 0.0, 0.0), # we use w-x-y-z convention for quaternions,
        scale = 1.0,
    ),
) """

""" franka = scene.add_entity(
    gs.morphs.URDF(
        file='urdf/panda_bullet/panda.urdf',
        fixed=True,
    ),
    #gs.morphs.MJCF(file="xml/franka_emika_panda/panda.xml"),
) """

scene.build()
for i in range(1000):
    scene.step()
