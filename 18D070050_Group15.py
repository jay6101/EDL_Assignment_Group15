import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

s_filepath = "../input/edl-data-2/EDL data final - Sheet1 (1).csv"

#############################################################
# Read the file into a variable s_data
s_data = pd.read_csv(s_filepath, index_col='Freq (Hz)')

# Set the width and height of the figure
plt.figure(figsize=(14,10))
plt.xscale('symlog')
# Add title
plt.title("|KGC| and |G| (dB) vs. Frequency (Hz)")

sns.lineplot(data=s_data['Magnitude of g'], label="| G |")

sns.lineplot(data=s_data['KGC in dB'], label="| KGC |")

# Add label for horizontal axis
plt.xlabel("Frequency (Hz)")
plt.ylabel("|KGC| and |G| (dB)")
#############################################################

# Set the width and height of the figure
plt.figure(figsize=(14,10))
plt.xscale('symlog')
plt.xlim([10,20000])
# Add title
plt.title("|KGC| vs. Frequency (Hz)")

sns.lineplot(data=s_data['KGC in dB'], label="| KGC |")
plt.axhline(y = 0, color = 'r', linestyle = 'dashed')


print(plt.axhline(y = 0, color = 'r', linestyle = 'dashed'))
print(plt.axvline(x = 1261.2, color = 'g', linestyle = '-'))
plt. scatter(1261.2, 0)
plt. annotate("(1261.2, 0)", (1261.2, 0))
# Add label for horizontal axis
plt.xlabel("Frequency (Hz)")
plt.ylabel("|KGC| (dB)")
#############################################################################################

# Set the width and height of the figure
plt.figure(figsize=(14,10))
plt.xscale('symlog')
plt.xlim([10,20000])
# Add title
plt.title("Phase KGC (degree) vs. Frequency (Hz)")

sns.lineplot(data=s_data['phase_c + phase G'][:7400], label="Phase of KGC")

print(plt.axhline(y = -131.85,color = 'r', linestyle = 'dashed'))
print(plt.axvline(x = 1261.2, color = 'g', linestyle = '-'))
plt. scatter(1261.2, -131.85)
plt. annotate("(1261.2, -131.85)", (1261.2, -131.85))

# Add label for horizontal axis
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase KGC (degree)")
#############################################################################################
# Set the width and height of the figure
plt.figure(figsize=(14,10))
plt.xscale('symlog')
plt.xlim([10,20000])
# Add title
plt.title("|KGC| vs. Frequency (Hz)")

sns.lineplot(data=s_data['KGC in dB'], label="| KGC |")



plt.axhline(y = -1.46,color = 'r', linestyle = 'dashed')
plt.axhline(y = -11.06,color = 'y', linestyle = 'dashed')
plt.axhline(y = -8.79,color = 'g', linestyle = 'dashed')

plt.axvline(x = 1904.08, color = 'r', linestyle = '-')
plt.axvline(x = 4156.40, color = 'y', linestyle = '-')
plt.axvline(x = 7220.19, color = 'g', linestyle = '-')

plt. scatter(1904.08, -1.46)
plt. annotate("(1904.08, -1.46)", (1904.08, -1.46))

plt. scatter(4156.40,-11.06)
plt. annotate("(4156.40,-11.06)", (4156.40,-11.06))

plt. scatter(7220.19, -8.79)
plt. annotate("(7220.19, -8.79)", (7220.19, -8.79))

plt.xlabel("Frequency (Hz)")
plt.ylabel("|KGC| (dB)")
#############################################################################################
# Set the width and height of the figure
plt.figure(figsize=(14,10))
plt.xscale('symlog')
plt.xlim([10,20000])
# Add title
plt.title("Phase KGC (degree) vs. Frequency (Hz)")


sns.lineplot(data=s_data['phase_c + phase G'][:7400], label="Phase of KGC")

plt.axhline(y = -180,color = 'r', linestyle = 'dashed')
plt.axhline(y = -540,color = 'y', linestyle = 'dashed')
plt.axhline(y = -900,color = 'g', linestyle = 'dashed')

plt.axvline(x = 1904.08, color = 'r', linestyle = '-')
plt.axvline(x = 4156.40, color = 'y', linestyle = '-')
plt.axvline(x = 7220.19, color = 'g', linestyle = '-')

plt. scatter(1904.08, -180)
plt. annotate("(1904.08, -180)", (1904.08, -180))

plt. scatter(4156.40, -540)
plt. annotate("(4156.40, -540)", (4156.40, -540))

plt. scatter(7220.19, -900)
plt. annotate("(7220.19, -900)", (7220.19, -900))

# Add label for horizontal axis
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase KGC (degree)")
#############################################################################################
# Set the width and height of the figure
plt.figure(figsize=(14,10))
plt.xscale('symlog')
# Add title
plt.title("Phase KGC (degree) vs. Frequency (Hz)")

sns.lineplot(data=s_data['phase_c + phase G'][:7400], label="Phase of KGC")

print(plt.axhline(y = -131.85,color = 'r', linestyle = 'dashed'))
print(plt.axvline(x = 1261.2, color = 'g', linestyle = '-'))
plt. scatter(1261.2, -131.85)
plt. annotate("(1261.2, -131.85)", (1261.2, -131.85))

# Add label for horizontal axis
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase KGC (degree)")
#############################################################################################
# Set the width and height of the figure
plt.figure(figsize=(14,10))
plt.xscale('symlog')
# Add title
plt.title("B/V (dB) vs. Frequency (Hz)")

sns.lineplot(data=s_data['B/V'], label="B/V")



# Add label for horizontal axis
plt.xlabel("Frequency (Hz)")
plt.ylabel("B/V (dB)")
plt.grid()
#############################################################################################

# Set the width and height of the figure
plt.figure(figsize=(14,10))
plt.xscale('symlog')
# Add title
plt.title("B/N (dB) vs. Frequency (Hz)")

sns.lineplot(data=s_data['B/N'], label="B/N")


# Add label for horizontal axis
plt.xlabel("Frequency (Hz)")
plt.ylabel("B/N (dB)")
plt.grid()
