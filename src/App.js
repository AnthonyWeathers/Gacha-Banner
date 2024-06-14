// making a gacha banner

import './styles.css';

import { useState, useEffect } from 'react';

function Summon({ onPageChange, summon }) {
    return (
      <div className='page' onClick={() => onPageChange('page1')} style={{ cursor: 'pointer' }}>
        {summon && <img className='img' src={summon} alt="1x summon result" />}
    </div>
    );
}

function Summon10x({ onPageChange, summons }) {
    return (
      <div className='page' onClick={() => onPageChange('page1')} style={{ cursor: 'pointer' }}>
        <div className="summons-grid">
          {summons && summons.map((summon, index) => (
            <div key={index} className="summon-item">
              <img src={summon} alt='summon result ${index}' className="summon-image" />
            </div>
          ))}
        </div>
    </div>
    );
}

function Banner({ onPageChange, banner, fiveStarOptions, onChange }) {
  return (
      <div>
        <section className='btns'>
            <button className='btn' onClick={() => onPageChange('page2')}>Summon 1x</button>
            <button className='btn' onClick={() => onPageChange('page3')}>Summon10x</button>
        </section>

        <DropDownMenu banner={banner} fiveStarOptions={fiveStarOptions} onChange={onChange}/>
      </div>
  );
}

const DropDownMenu = ({banner, fiveStarOptions, onChange}) => {
    return (
        <select value={banner} onChange={onChange}>
          {fiveStarOptions.map((fiveStarOption) => (
            <option key={fiveStarOption.url} value={fiveStarOption.url}>
              {fiveStarOption.title}
            </option>
          ))}
        </select>
    );
}

export default function Jukebox() {
  const [fiveStar, setFiveStar] = useState(null)
  const [currentPage, setCurrentPage] = useState('page1');
  const [banner, setBanner] = useState("https://pbs.twimg.com/media/FTiE2OZUEAEbyAV?format=jpg&name=900x900")

  const [summon, setSummon] = useState(null)
  const [summons, setSummons] = useState(null)

  const fiveStarGachaItems = [
    { title: 'Seele', url: 'https://pbs.twimg.com/media/FTiE2OZUEAEbyAV?format=jpg&name=900x900'},
    { title: 'Robin', url: 'https://pbs.twimg.com/media/GIcIXiqXIAAN97R?format=jpg&name=medium' },
    { title: 'Huohuo', url: 'https://pbs.twimg.com/media/F67FpP7aMAANzo4?format=jpg&name=medium'},
    { title: 'Acheron', url: 'https://pbs.twimg.com/media/GEf8B8ZbQAAM0tq?format=jpg&name=medium'},
    { title: 'Argenti', url: 'https://pbs.twimg.com/media/F7AJlx0aUAAAF4V?format=jpg&name=medium'},
    { title: 'Adventurine', url: 'https://pbs.twimg.com/media/GElKFNobAAAeKba?format=jpg&name=medium'},
    { title: 'Black Swan', url: 'https://pbs.twimg.com/media/GBHpnjhbAAA1mBg?format=jpg&name=medium'},
    { title: 'Blade', url: 'https://pbs.twimg.com/media/FwyNoqmXoAQFtSR?format=jpg&name=medium'},
    { title: 'Dan Heng * Imbibitor Lunae', url: 'https://pbs.twimg.com/media/F0Kh6dzagAEMNMx?format=jpg&name=medium'},
    { title: 'Dr. Ratio', url: 'https://pbs.twimg.com/media/F9vWzJoasAABkyr?format=jpg&name=medium'},
    { title: 'Fu Xuan', url: 'https://pbs.twimg.com/media/F0PyCXjaYAAUIg6?format=jpg&name=medium'},
    { title: 'Jing Yuan', url: 'https://pbs.twimg.com/media/Fv-2prUaQAABmde?format=jpg&name=medium'},
    { title: 'Jingliu', url: 'https://pbs.twimg.com/media/F3izd1FbsAAt0PC?format=jpg&name=medium'},
    { title: 'Kafka', url: 'https://pbs.twimg.com/media/Fw3XWsyagAEmEJL?format=jpg&name=medium'},
    { title: 'Luocha', url: 'https://pbs.twimg.com/media/FzR9yOJXoAIs_qj?format=jpg&name=medium'},
    { title: 'Ruan Mei', url: 'https://pbs.twimg.com/media/F9vQImPaUAANvhK?format=jpg&name=medium'},
    { title: 'Silver Wolf', url: 'https://pbs.twimg.com/media/FxmYj8EWwAIing9?format=jpg&name=medium'},
    { title: 'Sparkle', url: 'https://pbs.twimg.com/media/GBR5E3faMAAoVAn?format=jpg&name=medium'},
    { title: 'Topaz & Numby', url: 'https://pbs.twimg.com/media/F3n9T_iaEAAr7M8?format=jpg&name=medium'}
  ];

  useEffect( () => {
    updateBanner();
    const selected = fiveStarGachaItems.find(item => item.url === banner);
    setFiveStar(selected);
  }, [banner]);

  useEffect( () => {
    if(currentPage === 'page2') {
      fetch(`http://localhost:5000/summon/${fiveStar?.title}`)
        .then(response => response.json())
        .then(data => setSummon(data.summon))
        .catch(error => console.error('Error fetching the 1x summon result:', error));
    } else if(currentPage === 'page3') {
      fetch(`http://localhost:5000/summons/${fiveStar?.title}`)
        .then(response => response.json())
        .then(data => setSummons(data.summons))
        .catch(error => console.error('Error fetching the 10x summon result:', error));
    }
  }, [currentPage]);

  const updateBanner = () => {
    document.body.style.backgroundImage = `url(${banner})`;
  }

  const handleChange = event => {
    setBanner(event.target.value);
  }

  const handlePageChange = (page) => {
    setCurrentPage(page);
    if(page === 'page1') {
      updateBanner()
    } else {
      document.body.style.backgroundImage = 'none';
      console.log(summon)
    }
  };

    return (<>

        {currentPage === 'page1' && (
          <Banner onPageChange={handlePageChange} banner={banner} fiveStarOptions={fiveStarGachaItems} onChange={handleChange} />
        )}
        {currentPage === 'page2' && <Summon onPageChange={handlePageChange} summon={summon} />}
        {currentPage === 'page3' && <Summon10x onPageChange={handlePageChange} summons={summons} />}
    </>
    );

  }