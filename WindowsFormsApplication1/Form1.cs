using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using AForge.Video;
using AForge.Video.DirectShow;
using AForge.Vision;
using AForge.Vision.Motion;
namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        private IVideoSource source = null;
        static BlobCountingObjectsProcessing bc = new BlobCountingObjectsProcessing();
        MotionDetector det=new MotionDetector(new SimpleBackgroundModelingDetector(),bc);
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            
            FileVideoSource fs=new FileVideoSource("d:\\motion1.avi");
            source=fs;
            videoSourcePlayer1.VideoSource = new AsyncVideoSource(source);
            //source.Start();
            videoSourcePlayer1.Start();
        }

        private void videoSourcePlayer1_Click(object sender, EventArgs e)
        {
        
        }
        int i=0;
        private void videoSourcePlayer1_NewFrame(object sender, ref Bitmap image)
        {
            det.ProcessFrame(image);
            image.Save("d:\\frames\\" + i.ToString() + ".bmp");
            i++;
        }
    }
}
