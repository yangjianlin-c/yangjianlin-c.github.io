# Use flogate_cl Command convert xml to pdml 



1. set up the FloTHERM environment

   Start the command prompt with "run as administrator", then run

   ```
   cd "C:\Program Files\MentorMA\flosuite_v12\flotherm\WinXP\bin"
   flotherm -env
   ```

2.  Then convert xml as below:

   ```
   flogate_cl -i xml -r C:\Users\q19439\Desktop\New folder\folded_fin_heat_sink.xml -o pdml -w C:\test.pdml
   ```


