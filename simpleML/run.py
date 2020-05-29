"""
Usage:
    main.py
    main.py 
    main.py <nickname> <analysisid> <input_vcf_path>[--plots=<True/False>] [--report_format=<True/False>] [--yamlspec=<path-config-file>] [--configspec=<path--yaml-config-file>]
    main.py -h|--help
    main.py -v|--version
    main.py <input_vcf_path> -i|--interactive-analysis
Options:
    <name>  Optional name argument.
    -h --help  Show this screen.
    -v --version  Show version.
    --report_format Output format of required reports
    --plots Set True or False , default is False. True will create corresponding plots
    --configspec path of config file referring to indepth analysis report and plot control
    --yamlspec path of yaml file referring to indepth analysis report and plot control
"""

from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('SimpleML'))


try:
    output_folder = "{}/{}/{}/outputs/{}/".format(config['user_name'], config['analysis_name'], config['user_selected_model'], start_date)
    os.makedirs(output_folder)
except FileExistsError:
    # directory already exists
    pass

# backup config
# from shutil import copyfile
# copyfile(src, dst)