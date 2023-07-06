from pyglet.graphics.shader import Shader, ShaderProgram
import numpy as np

vertex_source = """
    #version 330
    uniform mat4 projection;
    uniform float dropsize;
    
    in vec3 position;
    in vec4 colors;
    out vec4 vertex_colors;
    
    void main()
    {
        gl_PointSize = dropsize;
        gl_Position = projection * vec4(position, 1.0);
        vertex_colors = colors;
    }
"""

fragment_source = """
    #version 330

    in vec4 vertex_colors;
    out vec4 outColor;
    
    void main()
    {
        outColor = vertex_colors;
    }
"""

vert_shader = Shader(vertex_source, 'vertex')
frag_shader = Shader(fragment_source, 'fragment')
program = ShaderProgram(vert_shader, frag_shader)
