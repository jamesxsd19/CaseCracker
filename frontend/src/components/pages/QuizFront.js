import React from 'react';
import '../../App.css';
import { QuizButton } from '../QuizButton';
import image from '../scotus_images.png';
import '../QuizFront.css';
import MySurvey from './surveys/surveyTypeone';
import styled from 'styled-components';

// Button for Quiz Start
const QuizB = styled.button`
  padding: 8px 20px;
  border-radius: 5px;
  outline: none;
  border: none;
  cursor: pointer;
  background-color: #512D21;
  color: #ffffff;
  padding: 8px 20px;
  border: 1px solid var(--primary);
  transition: all 0.3s ease-out;
  padding: 12px 26px;
  font-size: 20px;
  margin: 0px 5px

`
// This is the front page for the survey, where the user starts the
// self test 
function QuizFront() {
  return (
    <div className='quizfront-container'>
      <div className='quizfrontbox'>
        <h1>Political Self Leaning Test</h1>
      </div>

      <div className='quizfrontsmallbox'>
        <p> This survey contains a series of questions about your own political leaning. You will be given a list of statements and 
          you must select whether you agree or disagree. </p>
      </div>

      <div className='quizfront-btns'>
          {/* <QuizButton
          className='btn'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
          >
            Begin Quiz
          </QuizButton> */}
          <a href = './Survey'>
            <QuizB> Begin Quiz </QuizB>
          </a>
        </div>
    </div>
  );
}

export default QuizFront;