# Monitor-and-Record-drink-water-by-using-MTCNN-Facenet-YOLOv8pose
*(This AI system is built for a smart water bottle, which is capable of tracking the drinking activities of students in a class or family members.)*
* The first why an basic acctivy like drink water need to monitored and recorded, it included 3 mainpoints:
  * The human body is comprised of 70% water, making hydration an essential aspect of everyone's health.
  * In reality, we tend to overindulge in soft drink rather than opting for plain water and often only resorting to drinking water when thirst strikes, leading to our body not getting enough water every day
  * The failure to consume an adequate amount of water is a primary cause of numerous health conditions such as: constipation, gout, electrolyte disorders, especially kidney failure
    
__The mentioned points help you understand the importance of drinking water, and this system will help you track your water intake throughout the day, enabling you to adjust and ensure that you provide your body with an adequate amount of water.__

## How this system work?
### 1. Face recognition by MTCNN and Facenet
* For example, our "smart water purifier" use monitor in a classroom, it need to know who student come to take cup of water, therefore we need use face recognition to take information and record it to system
* First we use MTCNN to detected face of a student
 ![image](https://github.com/n1ne1903/Monitor-and-Record-drink-water-by-using-MTCNN-Facenet-YOLOv8pose/assets/141629048/42b3e0a0-b2ad-43fe-bb75-566340363749)
* Then use Facenet to check who is that student
  
  ![image](https://github.com/n1ne1903/Monitor-and-Record-drink-water-by-using-MTCNN-Facenet-YOLOv8pose/assets/141629048/2c637d1a-4580-40fe-80d4-f59d3206f105)

### 2. Drink water using YOLOv8pose
* After face recognition, we need to know is that student drink water or not. And to do that I use pretrain of YOLOv8pose to train my dataset
![train_batch2](https://github.com/n1ne1903/Monitor-and-Record-drink-water-by-using-MTCNN-Facenet-YOLOv8pose/assets/141629048/cbcfd8df-51ec-4ff5-ad98-73de10a1babe)
*(Training process)*
![val_batch0_pred](https://github.com/n1ne1903/Monitor-and-Record-drink-water-by-using-MTCNN-Facenet-YOLOv8pose/assets/141629048/43c92604-5e9f-4433-9b28-86e7e110aa0f)
*(Test Validation dataset)*

### 3. Record and report 
* When has model to verify student and detection drink water, I set to model model face recognition go first and if and only if a face verification succesfull, model detected drink water allow to run
* Here is output I have after run two model:
  
![image](https://github.com/n1ne1903/Monitor-and-Record-drink-water-by-using-MTCNN-Facenet-YOLOv8pose/assets/141629048/0f272608-99e1-4bbb-b85f-45e79479e304)
* Now I need to save it into a file csv and have result like that:

![image](https://github.com/n1ne1903/Monitor-and-Record-drink-water-by-using-MTCNN-Facenet-YOLOv8pose/assets/141629048/e7bf9d1c-3ab6-4fb6-a5fd-d476a2db23b3)

* The last step is upload this output.csv to a web or app for teacher or parents to monitor their students:

 ![image](https://github.com/n1ne1903/Monitor-and-Record-drink-water-by-using-MTCNN-Facenet-YOLOv8pose/assets/141629048/e67d6227-1a6c-4141-aca7-f4db97a5d85a)


* This is __Streamlit__ and you can see it record students "Lê Bảo Lâm" drink water 2 times today

## How to use this system?
