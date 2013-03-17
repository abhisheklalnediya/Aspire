'''
Created on 07-Feb-2012
@author: abhisheklal
'''
from opencv import highgui
import cv
import sys
class accessingcam(object):
    def startcam(self):
        image=None
        frame=None
    
        capture=cv.CreateCameraCapture (-1)
        overlay = cv.CreateImage((400,400), 8, 3)
        
        
        cv.Rectangle(overlay,(0,0),(400,400),cv.Scalar(0,0,225))
        #highgui.cvNamedWindow ('Aspire',CV_WINDOW_AUTOSIZE)
        #highgui.cvNamedWindow ('Aspire~orginal',highgui.CV_WINDOW_AUTOSIZE)
        b=0
        g=0
        r=0
        f=0
        x=0
        y=0
        print "Position the object above the square and Press any key to set the colour."
        while 1:
            frame=cv.QueryFrame(capture)    
            image=cv.CreateImage((400,400),8,3)
            redu=cv.CreateImage((100,100),8,1)
            
            cv.Resize(frame,image)
            cv.Flip(image,image,1)
            
            
            grey=cv.CreateImage(cv.GetSize(image),8,1)#size,depth,channels
            eig=cv.CreateImage(cv.GetSize(image),32,1)
            tmp=cv.CreateImage(cv.GetSize(image),32,1)    
            imghsv=cv.CreateImage(cv.GetSize(image),8,3)
            imghsv1=cv.CreateImage(cv.GetSize(image),8,3)
            imgtresh=cv.CreateImage(cv.GetSize(image),8,1)
            imgtreshc=cv.CreateImage(cv.GetSize(image),8,3)
               #imaget=cv2.CreateImage((400,400),8,1)
            
            cv.CvtColor (image, imghsv1,cv.CV_RGB2HSV)
            cv.CvtColor (image, imghsv,cv.CV_BGR2HSV)
            cv.InRangeS(imghsv1, cv.Scalar(b-20, g-40,r-40), cv.Scalar(b+20,g+40,r+40), imgtresh);
            cv.CvtColor(imgtresh,imgtreshc,cv.CV_GRAY2BGR)
            
            #pixel_value = cv.Get2D(imghsv1, 0, 0)
                # Since OpenCV loads color images in BGR, not RGB
                
                #print repr(b - pixel_value[0]) + " " +  repr(g - pixel_value[1]) + " " + repr(r - pixel_value[2])
                
            #b = pixel_value[0]
            #g = pixel_value[1]
            #r = pixel_value[2]
            #print repr(b) + " " + repr(g)  + " " + repr(r) + " " + repr(g+b)
            
            #cv.Copy (frame, image)
            #cv.CvtColor (image, grey, cv._RGB2GRAY)
            #cv.CvtColor (grey,image, cv._GRAY2RGB)
            
            if f==0 :
                c=0
                b=0
                g=0
                r=0
                for i in xrange(395,400) :
                    for j in xrange(395,400) :
                        c+=1
                        pixel_value = cv.Get2D(imghsv1, i, j)
                        b += pixel_value[0]
                        g += pixel_value[1]
                        r += pixel_value[2]
                        cv.Rectangle(image,(i,j),(i,j),cv.Scalar(0,0,225))
                        print repr(pixel_value[0]) + ","+repr(pixel_value[1]) + ","+repr(pixel_value[2]) + ",\t",
                        
                    print    ""
                b/=c
                g/=c
                r/=c    
                print "\n "+repr(c)+"\t"+repr(b) + "\t" + repr(g)  + "\t" + repr(r)  
            else :
                 
                
                
                points = [[],[]]    
            
                moments = cv.Moments(imgtresh, 0) 
                area = cv.GetCentralMoment(moments, 0, 0)
                
                
            
            #there can be noise in the video so ignore objects with small areas 
                if(area > 10000): 
                    #determine the x and y coordinates of the center of the object 
                    #we are tracking by dividing the 1, 0 and 0, 1 moments by the area 
                    #print "area " + repr(area)
                    x = cv.GetSpatialMoment(moments, 1, 0)/area 
                    y = cv.GetSpatialMoment(moments, 0, 1)/area 
                
                
                              
                    cv.Circle(overlay, (int(x), int(y)),3 , (0, 255, 255),)
                    cv.Circle(imgtreshc, (int(x), int(y)), 3, (r, g, b), 1)                 
                    cv.Add(image, overlay, image) 
                        #add the thresholded image back to the img so we can see what was  
                        #left after it was applied 
                        #cv.Merge(imgtresh, None, None, None, image)
            
                        #for p in points[1]:
                            #print p.x,"asdsd";
                
                            #cv.Circle(imgtreshc,(int(p.x),int(p.y)),3,cv.Scalar(r,g,b,0),-1,8,0)
                    #cv.ShowImage ('Aspire~Treshold', imgtreshc)
                    
                    # cv.ShowImage ('hsv1', overlay)
                    #cv.Resize(imgtresh,redu);
           
            cv.ShowImage ('Aspire-Treshold', imgtresh)
            cv.ShowImage ('Aspire-Cam', image)
        
            c=cv.WaitKey(10)
            if c<>-1 :
                
                if c==1048675:
                    f=0;
                    print "Selecting New color."
                else :
                    if c==1048603:
                        print("Exiting...");
                        sys.exit()
                    else :
                        print "Press c to set a new color."
                        f=1
                    
                