import dolfin as fem
import pygmsh as pg
import meshio

def gmsh_to_xdmf(mesh):
    # Export to dolfin .xml
    meshio.write("/tmp/mesh.xdmf",
        meshio.Mesh(points= mesh.points,
                    cells = dict(triangle= mesh.cells[0].data),
                    ),
    )

    # Load from dolfin .xml file
    mesh = fem.Mesh()
    with fem.XDMFFile('/tmp/mesh.xdmf') as infile:
        infile.read(mesh)

    return mesh

def disk(x, y= 1., l= 0.1):
    geom = pg.opencascade.Geometry(
    )

    geom.add_disk((0., 0., 0.), 1., radius1= y, char_length= l)

    mesh = pg.generate_mesh(geom,
        prune_z_0= True, verbose= 0, remove_lower_dim_cells= True,
    )

    mesh = gmsh_to_xdmf(mesh)

    mesh.scale(x)

    return mesh