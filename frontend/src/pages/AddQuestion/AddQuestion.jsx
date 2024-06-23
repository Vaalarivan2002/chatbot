import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const AddQuestion = () => {
    const navigate = useNavigate();
    const [qaPair, setQaPair] = useState({
        'question': '',
        'answer': '',
    });

    const handleChange = (args) => {
        let prevState = qaPair;
        prevState[args.key] = args.value;
        setQaPair({ ...prevState });
    };

    const handleSubmit = async () => {
        if (qaPair['question'] === '') {
            window.alert('Please type a valid question.');
            return;
        } else if (qaPair['answer'] === '') {
            window.alert('Please type a valid answer.');
            return;
        }

        // add qa pair to DB
        await axios.post('http://localhost:8000/admin-api/add-new-question/', {
            question: qaPair['question'],
            answer: qaPair['answer'],
        },
        )
            .then(() => navigate('/'));
    };

    return (<>
    <div>
        <div>
            <label htmlFor="question">Question: </label>
                <input type="text" id="question" required={true} aria-required={'true'} onChange={(e) => {
                    handleChange({
                        key: 'question',
                        value: e.target.value,
                    })
                }} />
        </div>
        <div>
            <label htmlFor="answer">Answer: </label>
                <input type="text" id="answer" required={true} aria-required={'true'} onChange={(e) => {
                    handleChange({
                        key: 'answer',
                        value: e.target.value,
                    })
                }} />
        </div>
        <button onClick={() => handleSubmit()}>Add question</button>
    </div>
    
    </>);
};

export default AddQuestion;