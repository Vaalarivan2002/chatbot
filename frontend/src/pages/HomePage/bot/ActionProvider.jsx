import React from 'react';
import axios from 'axios';
import { inlineBlockDisplay, noneDisplay } from '../../../constants';

const ActionProvider = ({ createChatBotMessage, setState, children, setDisplay, setResults }) => {

  const updateState = (message) => {
    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, message],
    }));
  };

  const handleQuestion = async (question) => {
    let answerResponse = '';

    setDisplay((display) => ({
      ...display,
      regenerateButtonDisplay: noneDisplay,
      satisfiedWithAnswerDisplay: noneDisplay,
      doubtAssistantDisplay: noneDisplay,
    }));
    axios.get('http://localhost:8000/api/answers/', {
      params: {
        question: question, 
      },
    })
      .then(response => {
        answerResponse = response.data.answers;
        setResults(answerResponse);
        
        const botMessage = createChatBotMessage(answerResponse[0]);
        
        updateState(botMessage);

        setDisplay((display) => ({
          ...display,
          regenerateButtonDisplay: inlineBlockDisplay,
        }));
      })
      .catch(error => {
        console.error('There was an error!', error);
      });
  };

  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          actions: {
            handleQuestion,
          },
        });
      })}
    </div>
  );
};

export default ActionProvider;