## Technical Notes
- Used the `pynput` library to capture keystrokes.
- Stored output in a local text file.
- Can run in the background without a visible console.
- Unable to implement presistance through startup folder or regex method as windows always flag it as malicious.

## Observations
- Type of exfiltration method matters a lot, sending information to random webserver flags AV but sending information to discord through webhook does not flag it.
- Command prompt appears when running the script by deafult, have to set the compile options to disable the cmd prompt in Nuitka, however this causes the standalone .exe file to be flagged but if we compile the .exe with dependencies sintead of a standalone one file, this will not not flag the AV.

## Security Insights
- Testing should be done in a VM without internet as Windows defender has somw cloud based signature uploading.
- Windows defender is very lenient in allowing unknown applications to run.
- A secondary AV is actually really necessary if installing or using unkown applications.

## Future potential additions
- Encrypting log files.
- Add peristance with future research.

## Refrences
- https://nuitka.net/user-documentation/
- https://pynput.readthedocs.io/en/latest/
