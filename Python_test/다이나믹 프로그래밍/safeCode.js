import util from '../modules/util';
import noticeModel from '../models/notice';
import userModel from '../models/user';

const noticeController = {
  /**
   * 학교 메뉴 조회
   */
  getSchoolMenu: async (req, res, next) => {
    //const idx = req.params.idx;
    try {
      const idx = req.schoolIdx;
      const data = await noticeModel.getSchoolMenu(idx);
      return res
        .status(200)
        .send(util.success(200, '학교 메뉴 조회 완료', data[0]));
    } catch (error) {
      next(error);
    }
  },
  /**
   * 키워드별 모아보기
   */
  getNoticeKeyword: async (req, res, next) => {
    try {
      const keyword_idx = req.params.keyword_idx;
      const school_idx = req.schoolIdx;

      const user_idx = req.userIdx;

      const paramPage = req.params.page;
      const page = (paramPage - 1) * 10;
      //const school_idx = 4;

      const data = await noticeModel.getNoticeKeyword(
        keyword_idx,
        school_idx,
        page
      );

      if (keyword_idx == -1) {
        const dataAll = await noticeModel.getAllNoticeKeyword(
          school_idx,
          user_idx,
          page
        );
        /*
            var keywordData=[];
            for (var i; i<arr.length; i++){
                keywordData.push(arr[i].keyword_idx);
            }
            console.log(keywordData);
            */

        if (dataAll.length === 0) {
          return res
            .status(400)
            .send(util.fail(400, '전체 모아보기 데이터가 없습니다.'));
        }

        if (paramPage % 2 === 0) {
          return res
            .status(200)
            .send(util.success(200, '키워드 전체 모아보기 조회 완료', dataAll));
        } else {
          const ad = await noticeModel.getAd();

          if (paramPage == 1) {
            const randomNumber = Math.floor(Math.random() * 4) + 2;
            dataAll.splice(randomNumber, 0, ad[0]);
            return res
              .status(200)
              .send(
                util.success(200, '키워드 전체 모아보기 조회 완료', dataAll)
              );
          } else {
            const randomNumber = Math.floor(Math.random() * 10) + 1;
            dataAll.splice(randomNumber, 0, ad[0]);
            return res
              .status(200)
              .send(
                util.success(200, '키워드 전체 모아보기 조회 완료', dataAll)
              );
          }
        }
      } else {
        const data = await noticeModel.getNoticeKeyword(
          keyword_idx,
          school_idx,
          page
        );

        if (data.length === 0) {
          return res
            .status(400)
            .send(util.fail(400, '모아보기 데이터가 없습니다.'));
        }

        if (paramPage % 2 === 0) {
          return res
            .status(200)
            .send(util.success(200, '키워드별 모아보기 조회 완료', data));
        } else {
          const newad = await noticeModel.getAd();

          if (paramPage == 1) {
            const randomNumber = Math.floor(Math.random() * 4) + 2;
            data.splice(randomNumber, 0, newad[0]);
            return res
              .status(200)
              .send(util.success(200, '키워드별 모아보기 조회 완료', data));
          } else {
            const randomNumber = Math.floor(Math.random() * 10) + 1;
            data.splice(randomNumber, 0, newad[0]);
            return res
              .status(200)
              .send(util.success(200, '키워드별 모아보기 조회 완료', data));
          }
        }
      }
    } catch (error) {
      next(error);
    }
  },

  /**
   * 학교 공지사항 타입별 보기
   */
  getSchoolNotice: async (req, res, next) => {
    try {
      const school_idx = req.schoolIdx;
      //const school_idx = 4;
      const menu_type = req.query.menu_type;
      const paramPage = req.query.page;
      const page = (paramPage - 1) * 10;
      //console.log(paramPage);
      const data = await noticeModel.getSchoolNotice(
        school_idx,
        menu_type,
        page
      );

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
    } catch (error) {
      next(error);
    }
  },
  /**
   * 학교별 전체 공지사항 보기
   */
  getAllSchoolNotice: async (req, res, next) => {
    try {
      const school_idx = req.schoolIdx;
      const paramPage = req.query.page;
      const page = (paramPage - 1) * 10;
      const data = await noticeModel.getAllSchoolNotice(
        school_idx,
        page
      );
      if (data.length === 0) {
        return res
          .status(400)
          .send(util.fail(400, '공지사항 데이터가 없습니다.'));
      }
      if (paramPage % 2 === 0) {
        return res
          .status(200)
          .send(util.success(200, '학교별 전체 공지사항 조회 완료', data));
      } else {
        const ad = await noticeModel.getAd();

        if (paramPage == 1) {
          const randomNumber = Math.floor(Math.random() * 4) + 2;
          data.splice(randomNumber, 0, ad[0]);
          return res
            .status(200)
            .send(util.success(200, '학교별 전체 공지사항 조회 완료', data));
        } else {
          const randomNumber = Math.floor(Math.random() * 10) + 1;
          data.splice(randomNumber, 0, ad[0]);
          return res
            .status(200)
            .send(util.success(200, '학교별 전체 공지사항 조회 완료', data));
        }
      }
    } catch (error) {
      next(error);
    }
  },
  /**
   * alarm: 가장 최신 공지사항을 가져온다
   */
  getLatestNotice: async (req, res, next) => {
    const school_idx = req.body.school_idx;

    try {
      const latestNotice = await noticeModel.getLatestNotice(school_idx);
      return res
        .status(200)
        .send(util.success(200, '최신 공지사항 조회 완료', latestNotice));
    } catch (error) {
      console.log(error);
      next(new Error('데이터베이스 조회 실패.'));
    }
  },
  /**
   * alarm: 특정 시간 이후에 저장된 공지사항들을 모두 가져온다
   */
  getRecentNotices: async (req, res, next) => {
    const school_idx = req.body.school_idx;
    const savedat = req.body.savedat;

    try {
      const recentNotices = await noticeModel.getRecentNotices(
        school_idx,
        savedat
      );
      return res
        .status(200)
        .send(util.success(200, '최근 공지사항 조회 완료', recentNotices));
    } catch (error) {
      console.log(error);
      next(new Error('데이터베이스 조회 실패.'));
    }
  }
};

export default noticeController;