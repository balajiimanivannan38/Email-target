import {useState} from "react";
export default function App(){
 const [token,setToken]=useState("");
 const login=async()=>{
  const r=await fetch("http://localhost:8000/login",{method:"POST"});
  const d=await r.json(); setToken(d.token);
 };
 return(
  <div style={{padding:20}}>
   <h1>Email AI</h1>
   <button onClick={login}>Login</button>
   <p>{token}</p>
  </div>
 );
}