import sys
import os


particle_dir = sys.argv[1]

print "Particle Directory:", particle_dir


# Check that AHF has already run
if not os.path.exists(particle_dir):
	print "Need to run AHF first before running MergerTree!"
	exit()

filenames = []

print "Getting particles files and creating needed lists for MergerTree"

# Get names of particle files
for file in os.listdir(particle_dir):
    if file.endswith(".AHF_particles"):
        filenames += [os.path.join(particle_dir, file)]

filenames.sort()
number = str(len(filenames))
# Create list of file names for MergerTree
particle_file_names = 'particle_file_names.txt'
with open(particle_file_names, 'w') as f:
    for item in filenames:
        f.write("%s\n" % item)

# Create output file names and write to txt file
output_names = []
for item in filenames[:-1]:
	output_names += [item[:-10]]

mtree_file_names = 'mtree_file_names.txt'
with open(mtree_file_names, 'w') as f:
    for item in output_names:
        f.write("%s\n" % item)

print "Running MergerTree"
# Now run MergerTree for the given files
my_command = 'MergerTree ' + number + particle_file_names + mtree_file_names
os.system(my_command)