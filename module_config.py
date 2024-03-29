
pandemonium_branch = 'master'

engine_repository = [ ['https://github.com/Relintai/pandemonium_engine.git', 'git@github.com:Relintai/pandemonium_engine.git'], 'pandemonium_engine', '' ]

# Relative to this script's directory
module_install_folder = './custom_modules/'

module_repositories = [
    #[ ['https://github.com/Relintai/entity_spell_system.git', 'git@github.com:Relintai/entity_spell_system.git'], 'entity_spell_system', '' ],
    #[ ['https://github.com/Relintai/ui_extensions.git', 'git@github.com:Relintai/ui_extensions.git'], 'ui_extensions', '' ],
    #[ ['https://github.com/Relintai/texture_packer.git', 'git@github.com:Relintai/texture_packer.git'], 'texture_packer', '' ],
    #[ ['https://github.com/Relintai/godot_fastnoise.git', 'git@github.com:Relintai/godot_fastnoise.git'], 'fastnoise', '' ],
    #[ ['https://github.com/Relintai/thread_pool.git', 'git@github.com:Relintai/thread_pool.git'], 'thread_pool', '' ],
    #[ ['https://github.com/Relintai/mesh_data_resource.git', 'git@github.com:Relintai/mesh_data_resource.git'], 'mesh_data_resource', '' ],
    #[ ['https://github.com/Relintai/mesh_utils.git', 'git@github.com:Relintai/mesh_utils.git'], 'mesh_utils', '' ],
    #[ ['https://github.com/Relintai/broken_seals_module.git', 'git@github.com:Relintai/broken_seals_module.git'], 'broken_seals_module', '' ],
    #[ ['https://github.com/Relintai/rtile_map.git', 'git@github.com:Relintai/rtile_map.git'], 'rtile_map', '' ],
]

removed_modules = [
    #[ ['https://github.com/Relintai/world_generator.git', 'git@github.com:Relintai/world_generator.git'], 'world_generator', '' ],
    #[ ['https://github.com/Relintai/terraman_2d.git', 'git@github.com:Relintai/terraman_2d.git'], 'terraman_2d', '' ],
    #[ ['https://github.com/Relintai/props.git', 'git@github.com:Relintai/props.git'], 'props', '' ],
]

addon_repositories = [
]

third_party_addon_repositories = [
]

# Relative to the engine directory
custom_module_folders = ''

slim_args = 'module_webm_enabled=no module_arkit_enabled=no module_visual_script_enabled=no module_gdnative_enabled=no module_mobile_vr_enabled=no module_theora_enabled=no module_xatlas_unwrap_enabled=no no_editor_splash=yes module_bullet_enabled=no module_camera_enabled=no module_csg_enabled=no module_denoise_enabled=no module_fbx_enabled=no module_gridmap_enabled=no module_hdr_enabled=no module_lightmapper_cpu_enabled=no module_raycast_enabled=no module_recast_enabled=no module_vhacd_enabled=no module_webxr_enabled=no'
