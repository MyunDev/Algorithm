  /**
   * 학교 공지사항 조회하기
   */
 getSchoolNotice: async (req, res, next) => {
    try {    
      
      const school_idx = req.schoolIdx;
      const menu_type = req.query.menu_type;
      const paramPage = req.query.page;
      const page = (paramPage - 1) * 10;

      const menuData = await noticeModel.getSchoolMenu(school_idx);
      const data = await noticeModel.getSchoolNotice(
        school_idx,
        menu_type,
        page
      );

      const allData = await noticeModel.getAllSchoolNotice(
        school_idx,
        page
      );

      //const flag = menuData.data.menu.includes("전체")
      const flag = true;
      if(flag === true){
        if (data.length === 0) {
            return res
            .status(400)
            .send(util.fail(400, '공지사항 데이터가 없습니다.'));
        }

        if (paramPage % 2 === 0) {
            //console.log("여기냐?")
            return res
            .status(200)
            .send(util.success(200, '공지사항 타입별 조회 완료', data));
        } else {
            const ad = await noticeModel.getAd();

            if (paramPage == 1) {
            const randomNumber = Math.floor(Math.random() * 4) + 2;
            //console.log(randomNumber);
            data.splice(randomNumber, 0, ad[0]);
            //console.log("야 좀 나와봐")
            return res
                .status(200)
                .send(util.success(200, '공지사항 타입별 조회 완료', data));
            } else {
            const randomNumber = Math.floor(Math.random() * 10) + 1;
            data.splice(randomNumber, 0, ad[0]);
            //console.log("아님 여기니?")
            return res
                .status(200)
                .send(util.success(200, '공지사항 타입별 조회 완료', data));
            }
        }
    }
    //학교 메뉴 중에 '전체' 메뉴가 없는 경우
    else {
      if (menu_type === "전체"){
        if (allData.length === 0) {
          return res
            .status(400)
            .send(util.fail(400, '공지사항 데이터가 없습니다.'));
        }
        if (paramPage % 2 === 0) {
          return res
            .status(200)
            .send(util.success(200, '학교별 전체 공지사항 조회 완료', allData));
        } else {
          const ad = await noticeModel.getAd();
  
          if (paramPage == 1) {
            const randomNumber = Math.floor(Math.random() * 4) + 2;
            allData.splice(randomNumber, 0, ad[0]);
            return res
              .status(200)
              .send(util.success(200, '학교별 전체 공지사항 조회 완료', allData));
          } else {
            const randomNumber = Math.floor(Math.random() * 10) + 1;
            allData.splice(randomNumber, 0, ad[0]);
            return res
              .status(200)
              .send(util.success(200, '학교별 전체 공지사항 조회 완료', allData));
          }
        }
      }
      else {
        if (data.length === 0) {
          return res
            .status(400)
            .send(util.fail(400, '공지사항 데이터가 없습니다.'));
        }
  
        if (paramPage % 2 === 0) {
          //console.log("여기냐?")
          return res
            .status(200)
            .send(util.success(200, '공지사항 타입별 조회 완료', data));
        } else {
          const ad = await noticeModel.getAd();
  
          if (paramPage == 1) {
            const randomNumber = Math.floor(Math.random() * 4) + 2;
            //console.log(randomNumber);
            data.splice(randomNumber, 0, ad[0]);
            //console.log("야 좀 나와봐")
            return res
              .status(200)
              .send(util.success(200, '공지사항 타입별 조회 완료', data));
          } else {
            const randomNumber = Math.floor(Math.random() * 10) + 1;
            data.splice(randomNumber, 0, ad[0]);
            //console.log("아님 여기니?")
            return res
              .status(200)
              .send(util.success(200, '공지사항 타입별 조회 완료', data));
          }
        }
      } 
    }
  } catch (error) {
      next(error);
    }
  }