extends Label

# Copyright (c) 2019 Péter Magyar
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

export(NodePath) var animation_player_path : NodePath = "AnimationPlayer"

export(Color) var damage_color : Color = Color.yellow
export(Color) var heal_color : Color = Color.green

var world_position : Vector2 = Vector2()
var animation_player : AnimationPlayer = null

func _ready() -> void:
	animation_player = get_node(animation_player_path) as AnimationPlayer
	
	animation_player.connect("animation_finished", self, "animation_finished")
	
	set_process(false)

func _process(delta):

	var new_pos : Vector2 = Vector2(world_position.x + rect_position.x / 2.0 - 8, world_position.y + rect_position.y)
	
	set_position(new_pos)
	

func damage(pos : Vector2, value : int, crit : bool) -> void:
	setup(pos, damage_color, value, crit)
	
func heal(pos : Vector2, value : int, crit : bool) -> void:
	setup(pos, heal_color, value, crit)

func setup(pos : Vector2, color : Color, value : int, crit : bool) -> void:
	world_position = pos
	
	text = str(value)
	add_theme_color_override("font_color", color)
	
	if crit:
		animation_player.play("crit")
	else:
		animation_player.play("normal")
		
	set_process(true)

func animation_finished(anim_name : String) -> void:
	queue_free()
