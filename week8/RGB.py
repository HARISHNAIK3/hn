input file='/home/rguktrkvalley/13.jpg';
imagedata=imread(inputfile);
redchannel=imagedata(:,:,1);
greenchannel=imagedata(:,:,2);
bluechannel=imagedata(:,:,3);

redoutputfile='red_channel.csv';
greenoutputfile='green_channel.csv';
blueoutputfile='blue_channel.csv';

cswrite(redoutputfile,redchannel);
cswrite(greenoutputfile,greenchannel);
cswrite(blueoutputfile,bluechannel);

disp('red,green and blue channels saved to separate csv files successfully!');
