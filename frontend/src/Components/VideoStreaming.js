import React from 'react' ;
import HOST_URL from '../config' ;

class VideoStreaming extends React.Component {
  render(){
    return(

      <div style={{display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center'}}>
      <h1>Hi Ameni !!</h1>
      <img style={{borderRadius:'25px',width:'80%',height:'80vh'}} src={HOST_URL+'/video_stream'} />
      </div>

    )
  }
}
export default VideoStreaming
