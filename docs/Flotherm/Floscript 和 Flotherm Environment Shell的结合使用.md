1.  Use the tables feature running directly in Flotherm and then export the values (you will get up to 15 significant digits).

2.  Create a floscript and run this in background mode to automatize the process:

1.  Open Flotherm
2.  Before loading the model start “Recording Floscript” and save it in a preferred location

![](https://support.sw.siemens.com/kbassets/external/MG620068/images/Picture1.png)  

3.  Run for 2 (few) iterations and export the results from tables
4.  “Stop recording” the floscript

![](https://support.sw.siemens.com/kbassets/external/MG620068/images/Picture2.png)  

5.  Close Flotherm

3.  The Floscript has now registered all the actions made during the set-up phase, run and results manipulation.

4.  Edit the floscript just created and change the number of outer iteration (check the first line of the file, should be there)

5.  Open the Flotherm Environment Shell

![](https://support.sw.siemens.com/kbassets/external/MG620068/images/Picture3.png)​​​​​​​  

1.  Write : **flotherm -b -f “here drag the floscript file”**
2.  Click enter to run.

6.  The Excel/csv file with all the data you want to have should be created and filled up with accurate values (up to 15 dig.)

The floscript file can be now used for other projects making the needed modification (project name, outer iteration etc..) using “ Play Floscript” or running the Flotherm Env. Shell.  

If needed, other Floscripts can be created following the steps above.