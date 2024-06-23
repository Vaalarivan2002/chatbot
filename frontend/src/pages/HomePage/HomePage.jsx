import { Chatbot } from 'react-chatbot-kit'
import 'react-chatbot-kit/build/main.css'
import config from './bot/config.js';
import MessageParser from './bot/MessageParser.jsx';
import ActionProvider from './bot/ActionProvider.jsx';
import { useRef, useState } from "react";
import { blockDisplay, flexDisplay, inlineBlockDisplay, inlineDisplay, noneDisplay } from "../../constants.js";
import { useNavigate } from 'react-router-dom';
import exportFromJson from 'export-from-json';

const HomePage = () => {
    const navigate = useNavigate();
    const [results, setResults] = useState([]);
    const [display, setDisplay] = useState({
        regenerateButtonDisplay: noneDisplay,
        endSessionDisplay: noneDisplay,
        satisfiedWithAnswerDisplay: noneDisplay,
        chatbotIconDisplay: inlineBlockDisplay,
        chatbotDisplay: noneDisplay,
        doubtAssistantDisplay: noneDisplay,
    });

    const handleRetry = () => {
        setDisplay((display) => ({
            ...display,
            regenerateButtonDisplay: noneDisplay,
            satisfiedWithAnswerDisplay: flexDisplay,
        }));
    };
    
    const whenUserSatisfied = () => {
        setDisplay((display) => ({
            ...display,
            satisfiedWithAnswerDisplay: noneDisplay,
        }));
    }

    const whenUserNotSatisfied = () => {
        setDisplay((display) => ({
            ...display,
            satisfiedWithAnswerDisplay: noneDisplay,
            doubtAssistantDisplay: inlineDisplay,
        }));
    }

    const endSession = () => {
        setDisplay((display) => ({
            ...display,
            endSessionDisplay: noneDisplay,
            chatbotIconDisplay: inlineBlockDisplay,
            chatbotDisplay: noneDisplay,
        }));
    };

    const retrieveLogs = () => {
        fetch('http://localhost:8000/admin-api/get-log/')
            .then((res) => res.json())
            .then(response => {
                let queriesLog = response.logs;
                const fileName = 'query_logs';
                const exportType = exportFromJson.types.csv;

                exportFromJson({ 
                    data: queriesLog, 
                    fileName, 
                    fields: ['log_id', 'question', 'responses', 'question_timestamp', 'time_to_generate_answer'],
                    exportType,
                });
            })
      };

    return (
        <>
            <button style={{display: display.chatbotIconDisplay}} onClick={
                () => setDisplay((display) => ({
                    ...display,
                    regenerateButtonDisplay: noneDisplay,
                    chatbotIconDisplay: noneDisplay,
                    chatbotDisplay: flexDisplay,
                    endSessionDisplay: blockDisplay,
                }))
            }>FAQ bot</button>
            <div style={{display: 'flex'}}>
                <div style={{display: display.chatbotDisplay, alignItems: 'center'}}>
                    <Chatbot
                        config={config}
                        messageParser={MessageParser}
                        actionProvider={(props) => 
                            <ActionProvider {...props} 
                                setDisplay={ setDisplay } 
                                setResults={ setResults }   
                            />}
                    />
                    &nbsp;
                    <button 
                        onClick={ handleRetry } 
                        style={{display: display.regenerateButtonDisplay, height: '50px', width: '100px',}}
                    >Regenerate result</button>

                    <div 
                        style={{display: display.satisfiedWithAnswerDisplay}} className='react-chatbot-kit-chat-bot-message'
                    >
                        <div>
                            <span>{ results[1] }</span>
                            <p style={{color: 'lightgreen',}}>Are you satisfied with the answer?</p>
                            <button onClick={whenUserSatisfied}>Yes</button>
                            <button onClick={whenUserNotSatisfied}>No</button>
                        </div>
                    </div>

                    <a 
                        href="mailto:pvaalarivan@gmail.com"
                        style={{color: 'white', display: display.doubtAssistantDisplay}}
                    >Mail to doubt support</a>
                
                </div>
                <div style={{display: 'flex', flexDirection: 'column'}}>
                    <button onClick={() => navigate('/add-question')}>Add new question</button>
                    <button onClick={retrieveLogs}>Download log file</button>
                </div>
            </div>
            
            <div style={{display: display.endSessionDisplay}}>
                <button onClick={endSession}>End session</button>
            </div>
        </>
    );
};

export default HomePage