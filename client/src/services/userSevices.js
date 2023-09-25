import axios from "axios"

// GET - Get All users 
export const GetAllUser = async (page,pageItems,search,sort)=>{
    const response = await axios.get(`http://127.0.0.1:5000/api/users/?page=${page}&pageSize=${pageItems}${search !== ""? `&search=${search}` :""}${sort !== "" ? `&sort=${sort}` :""}`)
    return response
}

export const getUser = async (id)=>{
    const response = await axios.get(`http://127.0.0.1:5000/api/users/${id}`)
    return response
}
