import React from 'react' ;
import HOST_URL from '../config' ;
import axios from 'axios' ;
import './stream.css' ;

class VideoStreaming extends React.Component {
   move_robot = (action)=>{
    let HOST_URL = 'http://127.0.0.1:5000'
    axios.get(HOST_URL+'/'+action).then(res=>{
      console.log(res);
    })
  }

  render(){
    return(

      <div style={{display:'flex',justifyContent:'space-around'}}>
      <div style={{width:'70%'}}>
          <h1>Hi Abdallah !!</h1>
          <img style={{width:'100%',height:'80vh'}} src={HOST_URL+'/video_stream'} />
      </div>
      <div style={{display:'flex',width:'25%',flexDirection:'column',alignItems:'center'}}>
      <h1>Control Panel</h1>
          <button class='btn' onMouseDown={()=>{this.move_robot('forward')}} onMouseUp={()=>{this.move_robot('stop')}}>Up</button>
          <div style={{display:'flex',width:'100%',justifyContent:'space-between'}}>
          <button class='btn' onMouseDown={()=>{this.move_robot('right')}} onMouseUp={()=>{this.move_robot('stop')}}>Right</button>
          <button class='btn' onMouseDown={()=>{this.move_robot('left')}} onMouseUp={()=>{this.move_robot('stop')}}>Left</button>
          </div>
          <button class='btn' onMouseDown={()=>{this.move_robot('backward')}} onMouseUp={()=>{this.move_robot('stop')}} >Bottom</button>
      </div>
      </div>

    )
  }
}
export default VideoStreaming
