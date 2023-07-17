import React from 'react'
import {AiFillGithub} from 'react-icons/ai'

const main = () => {

    const handleModal = () => {
      if(document.querySelector('#zo').value === '')
      {
        alert('Please fill all required fields');
      }
      else if(document.querySelector('#ln').value === '')
      {
        alert('Please fill all required fields');
      }
      else if(document.querySelector('#lc').value === '')
      {
        alert('Please fill all required fields');
      }
      else if(document.querySelector('#rf').value === '')
      {
        alert('Please fill all required fields');
      }
      else{
        document.querySelector('#modal-box').style.display = 'block'
        console.log(document.querySelector('#zo').value)
        calculate();
      }
      }
    
      const closeModal = () => {
        window.location.reload();
      }

      const calculate = () => {
        const zod = document.querySelector('#zo').value.toLowerCase();
        const rif = document.querySelector('#rf').value.toLowerCase();
        const luc = document.querySelector('#lc').value.toLowerCase();
        const output = document.querySelector('#mc')
        var zod1;
        var rif1;
        var luc1;
        if(zod === "taurus" )
        {
            zod1 = 1;
        }
        else if(zod === "leo" )
        {
            zod1 = 2;
        }
        else if(zod === "capricon" )
        {
            zod1 = 3;
        }
        else if(zod === "cancer" )
        {
            zod1 = 4;
        }
        else if(zod === "virgo" )
        {
            zod1 = 5;
        }
        else if(zod === "pisces" )
        {
            zod1 = 6;
        }
        else if(zod === "libra" )
        {
            zod1 = 7;
        }
        else if(zod === "scorpio" )
        {
            zod1 = 8;
        }
        else if(zod === "aries" )
        {
            zod1 = 9;
        }
        else if(zod === "aquarius" )
        {
            zod1 = 10;
        }
        else if(zod === "gemini" )
        {
            zod1 = 11;
        }
        else if(zod === "sagittarius" )
        {
            zod1 = 12;
        }
        if(rif === "yes" )
        {
            rif1 = 2;
        }
        else{
            rif1 = 1;
        }
        if(luc === "yes" )
        {
            luc1 = 2;
        }
        else{
            luc1 = 1; 
        }
        const zo= 1.92724406;
        const ln= 0.64827626;
        const lc= -20.59486577;
        const rf= -30.49577125;
        const intercept = 106.69244366169843;
        const ans = (zod1*zo)+((document.querySelector('#ln').value)*ln)+(rif1*rf)+(luc1*lc)+intercept;
         output.textContent = `Today your are ${Math.round(ans)} % lucky .`;
         console.log(zod1);
      }

      const Warning = () => {
        document.querySelector('#modal-box1').style.display = 'block'
      }

  return (
    <div>
    <form class="form">
     <div class="form-title"><span>Unlock Your Funky Fortune!</span></div>
      <div class="title-2"><span>ZODIAC LUCK METER</span></div>
      <div class="input-container">
        <input class="input-item" type="text" placeholder="Enter zodiac sign" id='zo' required/>
        <span> </span>
      </div>
      <section class="bg-stars">
        <span class="star"></span>
        <span class="star"></span>
        <span class="star"></span>
        <span class="star"></span>
        <span class="star"></span>
      </section>
      <div class="input-container">
        <input class="input-item" type="number" placeholder="Enter your lucky number" id='ln' required/>
      </div>
      <div class="input-container">
        <input class="input-item" type="text" placeholder="Followed the RITUAL ? (Yes/No)" id='rf' required/>
      </div>
      <div class="input-container">
        <input class="input-item" type="text" placeholder="Carry any good luck charms ? (Yes/No)" id='lc' required/>
      </div>
      <span class="submit" onClick={handleModal}>
        <span class="sign-text">PREDICT!</span>
      </span>  
   </form>
   <div id="modal-box" class="modal">
  <div class="modal-content">
      <h2>Voilà !</h2>
      <p id="mc">Please fill the required fields</p>
      <div class="ns" onClick={closeModal}>
         New Search ?
      </div>
  </div>
</div>
<div id="modal-box1" class="modal1">
  <div class="modal-content1">
      <h2 id='caution'>CAUTION!</h2>
      <p id="mc">The 'RITUAL' offers a sacrifice of an annoying cat. You can watch it by continuing. The content you about to watch might be disturbing. Continue at your own risk.</p>
      <div class="ns" >
        <a href="https://www.youtube.com/watch?v=B_vyALmAzjY&ab_channel=PatrickK" target='_blank'>Continue</a> 
      </div>
      <div class="ns" onClick={closeModal}>
         Go Back (Highly Suggested)
      </div>
  </div>
</div>
    <div class="signup-link" id="questions">
      <p class="up" onClick={Warning}>What is this damn RITUAL ?</p>
    </div>
    <a href="https://github.com/REC-1104/lucky-day-prediction-" target='_blank'><AiFillGithub class="github-icon" /></a>
    </div>
  )
}

export default main