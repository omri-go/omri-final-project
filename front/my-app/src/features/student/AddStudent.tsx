import React, { useState } from 'react'
import { addStudentAsync } from './studentSlice'
import { useAppSelector, useAppDispatch } from '../../app/hooks';

const AddStudent = () => {
    const dispatch = useAppDispatch();
    const [sname, setsname] = useState("")
    const [age, setage] = useState(0)
    return (
        <div>
            Add a new Student<br></br>
            Student name<input onChange={(e) => setsname(e.target.value)} />
            age:<input onChange={(e) => setage(+e.target.value)} />
            <button onClick={()=>dispatch(addStudentAsync({age,sname}))}>Add</button>
        </div>
    )
}
export default AddStudent