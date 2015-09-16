# Copyright 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# NOTE: this file is autogenerated by ffmpeg/chromium/scripts/generate_gyp.py


{
  'variables': {
    'conditions': [
      ['OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS"', {
        'c_sources': [
          'libavcodec/arm/blockdsp_init_neon.c',
          'libavcodec/arm/idctdsp_init_neon.c',
        ],
        'asm_sources': [
          'libavcodec/arm/blockdsp_neon.S',
          'libavcodec/arm/idctdsp_neon.S',
          'libavcodec/arm/mpegvideo_neon.S',
          'libavcodec/arm/simple_idct_neon.S',
        ],
      }],  # OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS"
      ['OS == "linux" and target_arch == "mipsel" and ffmpeg_branding == "ChromeOS"', {
        'c_sources': [
          'libavcodec/mips/blockdsp_init_mips.c',
          'libavcodec/mips/h263dsp_init_mips.c',
          'libavcodec/mips/idctdsp_init_mips.c',
          'libavcodec/mips/me_cmp_init_mips.c',
          'libavcodec/mips/mpegvideo_init_mips.c',
          'libavcodec/mips/pixblockdsp_init_mips.c',
          'libavcodec/mips/qpeldsp_init_mips.c',
          'libavcodec/mips/xvididct_init_mips.c',
        ],
      }],  # OS == "linux" and target_arch == "mipsel" and ffmpeg_branding == "ChromeOS"
      ['(OS == "linux" and target_arch == "ia32" and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "x64" and ffmpeg_branding == "ChromeOS")', {
        'c_sources': [
          'libavcodec/x86/blockdsp_init.c',
          'libavcodec/x86/fdct.c',
          'libavcodec/x86/fdctdsp_init.c',
          'libavcodec/x86/h263dsp_init.c',
          'libavcodec/x86/idctdsp_init.c',
          'libavcodec/x86/me_cmp_init.c',
          'libavcodec/x86/mpegvideo.c',
          'libavcodec/x86/mpegvideodsp.c',
          'libavcodec/x86/pixblockdsp_init.c',
          'libavcodec/x86/qpeldsp_init.c',
          'libavcodec/x86/simple_idct.c',
          'libavcodec/x86/xvididct_init.c',
        ],
        'asm_sources': [
          'libavcodec/x86/blockdsp.asm',
          'libavcodec/x86/h263_loopfilter.asm',
          'libavcodec/x86/idctdsp.asm',
          'libavcodec/x86/me_cmp.asm',
          'libavcodec/x86/pixblockdsp.asm',
          'libavcodec/x86/qpeldsp.asm',
          'libavcodec/x86/xvididct.asm',
        ],
      }],  # (OS == "linux" and target_arch == "ia32" and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "x64" and ffmpeg_branding == "ChromeOS")
      ['OS == "win" and target_arch == "x64"', {
        'asm_sources': [
          'libavutil/x86/emms.asm',
        ],
      }],  # OS == "win" and target_arch == "x64"
      ['OS == "mac"', {
        'c_sources': [
          'libavcodec/videotoolbox.c',
        ],
      }],  # OS == "mac"
      ['(OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS")', {
        'asm_sources': [
          'libavcodec/arm/h264cmc_neon.S',
          'libavcodec/arm/h264dsp_neon.S',
          'libavcodec/arm/h264idct_neon.S',
          'libavcodec/arm/h264qpel_neon.S',
        ],
      }],  # (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS")
      ['(OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "arm64" and ffmpeg_branding == "ChromeOS")', {
        'c_sources': [
          'libavcodec/neon/autorename_libavcodec_neon_mpegvideo.c',
        ],
      }],  # (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "arm64" and ffmpeg_branding == "ChromeOS")
      ['(OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "arm" and ffmpeg_branding == "ChromeOS")', {
        'c_sources': [
          'libavcodec/arm/blockdsp_init_arm.c',
          'libavcodec/arm/idctdsp_init_arm.c',
          'libavcodec/arm/idctdsp_init_armv5te.c',
          'libavcodec/arm/idctdsp_init_armv6.c',
          'libavcodec/arm/me_cmp_init_arm.c',
          'libavcodec/arm/mpegvideo_arm.c',
          'libavcodec/arm/mpegvideo_armv5te.c',
          'libavcodec/arm/pixblockdsp_init_arm.c',
        ],
        'asm_sources': [
          'libavcodec/arm/idctdsp_arm.S',
          'libavcodec/arm/idctdsp_armv6.S',
          'libavcodec/arm/jrevdct_arm.S',
          'libavcodec/arm/me_cmp_armv6.S',
          'libavcodec/arm/mpegvideo_armv5te_s.S',
          'libavcodec/arm/pixblockdsp_armv6.S',
          'libavcodec/arm/simple_idct_arm.S',
          'libavcodec/arm/simple_idct_armv5te.S',
          'libavcodec/arm/simple_idct_armv6.S',
        ],
      }],  # (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "arm" and ffmpeg_branding == "ChromeOS")
      ['(OS == "linux" and target_arch == "arm64" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm64" and ffmpeg_branding == "ChromeOS")', {
        'c_sources': [
          'libavcodec/aarch64/h264chroma_init_aarch64.c',
          'libavcodec/aarch64/h264dsp_init_aarch64.c',
          'libavcodec/aarch64/h264qpel_init_aarch64.c',
          'libavcodec/aarch64/imdct15_init.c',
          'libavcodec/aarch64/mpegaudiodsp_init.c',
        ],
        'asm_sources': [
          'libavcodec/aarch64/autorename_libavcodec_aarch64_h264cmc_neon.S',
          'libavcodec/aarch64/autorename_libavcodec_aarch64_h264dsp_neon.S',
          'libavcodec/aarch64/autorename_libavcodec_aarch64_h264idct_neon.S',
          'libavcodec/aarch64/autorename_libavcodec_aarch64_h264qpel_neon.S',
          'libavcodec/aarch64/imdct15_neon.S',
          'libavcodec/aarch64/mpegaudiodsp_neon.S',
        ],
      }],  # (OS == "linux" and target_arch == "arm64" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm64" and ffmpeg_branding == "ChromeOS")
      ['(OS == "linux" and target_arch == "mipsel" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "mipsel" and ffmpeg_branding == "ChromeOS")', {
        'c_sources': [
          'libavcodec/mips/aacdec_mips.c',
          'libavcodec/mips/aacpsdsp_mips.c',
          'libavcodec/mips/aacsbr_mips.c',
          'libavcodec/mips/h264chroma_init_mips.c',
          'libavcodec/mips/h264dsp_init_mips.c',
          'libavcodec/mips/h264qpel_init_mips.c',
          'libavcodec/mips/sbrdsp_mips.c',
        ],
      }],  # (OS == "linux" and target_arch == "mipsel" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "mipsel" and ffmpeg_branding == "ChromeOS")
      ['(OS == "android" and target_arch == "arm" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS")', {
        'asm_sources': [
          'libavcodec/arm/aacpsdsp_neon.S',
          'libavcodec/arm/sbrdsp_neon.S',
        ],
      }],  # (OS == "android" and target_arch == "arm" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS")
      ['OS == "win"', {
        'c_sources': [
          'compat/msvcrt/snprintf.c',
        ],
      }],  # OS == "win"
      ['(OS == "linux" and target_arch == "ia32" and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "ia32" and ffmpeg_branding == "ChromiumOS") or (OS == "linux" and target_arch == "x64" and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "x64" and ffmpeg_branding == "ChromiumOS")', {
        'c_sources': [
          'libavcodec/x86/flacdsp_init.c',
        ],
        'asm_sources': [
          'libavcodec/x86/flacdsp.asm',
        ],
      }],  # (OS == "linux" and target_arch == "ia32" and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "ia32" and ffmpeg_branding == "ChromiumOS") or (OS == "linux" and target_arch == "x64" and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "x64" and ffmpeg_branding == "ChromiumOS")
      ['(OS == "linux" and target_arch == "ia32" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "ia32" and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "x64" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "x64" and ffmpeg_branding == "ChromeOS") or (OS == "mac" and ffmpeg_branding == "Chrome") or (OS == "win" and ffmpeg_branding == "Chrome")', {
        'c_sources': [
          'libavcodec/x86/aacpsdsp_init.c',
          'libavcodec/x86/dct_init.c',
          'libavcodec/x86/h264_qpel.c',
          'libavcodec/x86/h264chroma_init.c',
          'libavcodec/x86/h264dsp_init.c',
          'libavcodec/x86/mpegaudiodsp.c',
          'libavcodec/x86/sbrdsp_init.c',
        ],
        'asm_sources': [
          'libavcodec/x86/aacpsdsp.asm',
          'libavcodec/x86/dct32.asm',
          'libavcodec/x86/h264_chromamc.asm',
          'libavcodec/x86/h264_chromamc_10bit.asm',
          'libavcodec/x86/h264_deblock.asm',
          'libavcodec/x86/h264_deblock_10bit.asm',
          'libavcodec/x86/h264_idct.asm',
          'libavcodec/x86/h264_idct_10bit.asm',
          'libavcodec/x86/h264_qpel_10bit.asm',
          'libavcodec/x86/h264_qpel_8bit.asm',
          'libavcodec/x86/h264_weight.asm',
          'libavcodec/x86/h264_weight_10bit.asm',
          'libavcodec/x86/imdct36.asm',
          'libavcodec/x86/qpel.asm',
          'libavcodec/x86/sbrdsp.asm',
        ],
      }],  # (OS == "linux" and target_arch == "ia32" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "ia32" and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "x64" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "x64" and ffmpeg_branding == "ChromeOS") or (OS == "mac" and ffmpeg_branding == "Chrome") or (OS == "win" and ffmpeg_branding == "Chrome")
      ['OS == "linux" and target_arch == "arm" and arm_neon == 1', {
        'c_sources': [
          'libavcodec/arm/hpeldsp_init_neon.c',
          'libavcodec/arm/vp8dsp_init_neon.c',
        ],
        'asm_sources': [
          'libavcodec/arm/h264pred_neon.S',
          'libavcodec/arm/hpeldsp_neon.S',
          'libavcodec/arm/vp3dsp_neon.S',
          'libavcodec/arm/vp8dsp_neon.S',
        ],
      }],  # OS == "linux" and target_arch == "arm" and arm_neon == 1
      ['(OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "arm" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and ffmpeg_branding == "ChromeOS")', {
        'c_sources': [
          'libavcodec/arm/h264chroma_init_arm.c',
          'libavcodec/arm/h264dsp_init_arm.c',
          'libavcodec/arm/h264qpel_init_arm.c',
        ],
        'asm_sources': [
          'libavcodec/arm/startcode_armv6.S',
        ],
      }],  # (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "arm" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and ffmpeg_branding == "ChromeOS")
      ['(OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromiumOS") or (OS == "linux" and target_arch == "arm" and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "arm" and ffmpeg_branding == "ChromiumOS")', {
        'c_sources': [
          'libavcodec/arm/flacdsp_init_arm.c',
        ],
        'asm_sources': [
          'libavcodec/arm/flacdsp_arm.S',
        ],
      }],  # (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromiumOS") or (OS == "linux" and target_arch == "arm" and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "arm" and ffmpeg_branding == "ChromiumOS")
      ['OS == "linux" and target_arch == "arm64"', {
        'c_sources': [
          'libavcodec/aarch64/fft_init_aarch64.c',
          'libavcodec/aarch64/h264pred_init.c',
          'libavcodec/aarch64/hpeldsp_init_aarch64.c',
          'libavcodec/aarch64/videodsp_init.c',
          'libavcodec/aarch64/vorbisdsp_init.c',
          'libavutil/aarch64/cpu.c',
          'libavutil/aarch64/float_dsp_init.c',
        ],
        'asm_sources': [
          'libavcodec/aarch64/autorename_libavcodec_aarch64_h264pred_neon.S',
          'libavcodec/aarch64/autorename_libavcodec_aarch64_hpeldsp_neon.S',
          'libavcodec/aarch64/fft_neon.S',
          'libavcodec/aarch64/mdct_neon.S',
          'libavcodec/aarch64/videodsp.S',
          'libavcodec/aarch64/vorbisdsp_neon.S',
          'libavutil/aarch64/float_dsp_neon.S',
        ],
      }],  # OS == "linux" and target_arch == "arm64"
      ['OS == "linux" and target_arch == "mipsel"', {
        'c_sources': [
          'libavcodec/mips/h264pred_init_mips.c',
          'libavcodec/mips/hpeldsp_init_mips.c',
          'libavcodec/mips/vp8dsp_init_mips.c',
          'libavutil/mips/float_dsp_mips.c',
        ],
      }],  # OS == "linux" and target_arch == "mipsel"
      ['OS == "linux" and ffmpeg_branding == "ChromeOS"', {
        'c_sources': [
          'libavcodec/acelp_filters.c',
          'libavcodec/acelp_pitch_delay.c',
          'libavcodec/acelp_vectors.c',
          'libavcodec/amrnbdec.c',
          'libavcodec/amrwbdec.c',
          'libavcodec/autorename_libavcodec_gsmdec.c',
          'libavcodec/autorename_libavcodec_mpegvideo.c',
          'libavcodec/autorename_libavcodec_mpegvideodsp.c',
          'libavcodec/autorename_libavcodec_simple_idct.c',
          'libavcodec/blockdsp.c',
          'libavcodec/celp_filters.c',
          'libavcodec/celp_math.c',
          'libavcodec/error_resilience.c',
          'libavcodec/exif.c',
          'libavcodec/faandct.c',
          'libavcodec/faanidct.c',
          'libavcodec/fdctdsp.c',
          'libavcodec/flvdec.c',
          'libavcodec/gsm_parser.c',
          'libavcodec/gsmdec_data.c',
          'libavcodec/h263.c',
          'libavcodec/h263_parser.c',
          'libavcodec/h263data.c',
          'libavcodec/h263dec.c',
          'libavcodec/h263dsp.c',
          'libavcodec/idctdsp.c',
          'libavcodec/intelh263dec.c',
          'libavcodec/ituh263dec.c',
          'libavcodec/jfdctfst.c',
          'libavcodec/jfdctint.c',
          'libavcodec/jrevdct.c',
          'libavcodec/lsp.c',
          'libavcodec/me_cmp.c',
          'libavcodec/mpeg4video.c',
          'libavcodec/mpeg4video_parser.c',
          'libavcodec/mpeg4videodec.c',
          'libavcodec/mpeg_er.c',
          'libavcodec/mpegpicture.c',
          'libavcodec/mpegutils.c',
          'libavcodec/mpegvideo_motion.c',
          'libavcodec/mpegvideodata.c',
          'libavcodec/msgsmdec.c',
          'libavcodec/pixblockdsp.c',
          'libavcodec/qpeldsp.c',
          'libavcodec/rl.c',
          'libavcodec/tiff_common.c',
          'libavcodec/xvididct.c',
          'libavformat/amr.c',
          'libavformat/avidec.c',
          'libavformat/gsmdec.c',
        ],
      }],  # OS == "linux" and ffmpeg_branding == "ChromeOS"
      ['(OS == "android" and target_arch == "arm" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "arm" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and ffmpeg_branding == "ChromeOS")', {
        'c_sources': [
          'libavcodec/arm/aacpsdsp_init_arm.c',
          'libavcodec/arm/mpegaudiodsp_init_arm.c',
          'libavcodec/arm/sbrdsp_init_arm.c',
        ],
        'asm_sources': [
          'libavcodec/arm/mpegaudiodsp_fixed_armv6.S',
        ],
      }],  # (OS == "android" and target_arch == "arm" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and arm_neon == 1 and ffmpeg_branding == "ChromeOS") or (OS == "linux" and target_arch == "arm" and ffmpeg_branding == "Chrome") or (OS == "linux" and target_arch == "arm" and ffmpeg_branding == "ChromeOS")
      ['(OS == "android" and target_arch == "arm") or (OS == "win")', {
        'c_sources': [
          'compat/strtod.c',
        ],
      }],  # (OS == "android" and target_arch == "arm") or (OS == "win")
      ['(OS == "android" and target_arch == "arm") or (OS == "linux" and target_arch == "arm" and arm_neon == 1)', {
        'c_sources': [
          'libavutil/arm/float_dsp_init_neon.c',
        ],
        'asm_sources': [
          'libavcodec/arm/autorename_libavcodec_arm_fft_neon.S',
          'libavcodec/arm/autorename_libavcodec_arm_mdct_neon.S',
          'libavcodec/arm/autorename_libavcodec_arm_vorbisdsp_neon.S',
          'libavcodec/arm/fft_fixed_neon.S',
          'libavcodec/arm/mdct_fixed_neon.S',
          'libavcodec/arm/rdft_neon.S',
          'libavutil/arm/autorename_libavutil_arm_float_dsp_neon.S',
        ],
      }],  # (OS == "android" and target_arch == "arm") or (OS == "linux" and target_arch == "arm" and arm_neon == 1)
      ['(OS == "linux" and target_arch == "ia32") or (OS == "linux" and target_arch == "x64") or (OS == "mac") or (OS == "win")', {
        'c_sources': [
          'libavcodec/x86/autorename_libavcodec_x86_videodsp_init.c',
          'libavcodec/x86/autorename_libavcodec_x86_vorbisdsp_init.c',
          'libavcodec/x86/constants.c',
          'libavcodec/x86/fft_init.c',
          'libavcodec/x86/h264_intrapred_init.c',
          'libavcodec/x86/hpeldsp_init.c',
          'libavcodec/x86/vp3dsp_init.c',
          'libavcodec/x86/vp8dsp_init.c',
          'libavutil/x86/autorename_libavutil_x86_cpu.c',
          'libavutil/x86/autorename_libavutil_x86_float_dsp_init.c',
          'libavutil/x86/lls_init.c',
        ],
        'asm_sources': [
          'libavcodec/x86/fft.asm',
          'libavcodec/x86/fpel.asm',
          'libavcodec/x86/h264_intrapred.asm',
          'libavcodec/x86/h264_intrapred_10bit.asm',
          'libavcodec/x86/hpeldsp.asm',
          'libavcodec/x86/videodsp.asm',
          'libavcodec/x86/vorbisdsp.asm',
          'libavcodec/x86/vp3dsp.asm',
          'libavcodec/x86/vp8dsp.asm',
          'libavcodec/x86/vp8dsp_loopfilter.asm',
          'libavutil/x86/cpuid.asm',
          'libavutil/x86/float_dsp.asm',
          'libavutil/x86/lls.asm',
        ],
      }],  # (OS == "linux" and target_arch == "ia32") or (OS == "linux" and target_arch == "x64") or (OS == "mac") or (OS == "win")
      ['(OS == "linux" and target_arch == "arm" and arm_neon == 1) or (OS == "linux" and target_arch == "arm")', {
        'c_sources': [
          'libavcodec/arm/h264pred_init_arm.c',
          'libavcodec/arm/hpeldsp_init_arm.c',
          'libavcodec/arm/hpeldsp_init_armv6.c',
          'libavcodec/arm/videodsp_init_arm.c',
          'libavcodec/arm/videodsp_init_armv5te.c',
          'libavcodec/arm/vp3dsp_init_arm.c',
          'libavcodec/arm/vp8dsp_init_arm.c',
          'libavcodec/arm/vp8dsp_init_armv6.c',
        ],
        'asm_sources': [
          'libavcodec/arm/hpeldsp_arm.S',
          'libavcodec/arm/hpeldsp_armv6.S',
          'libavcodec/arm/videodsp_armv5te.S',
          'libavcodec/arm/vp8_armv6.S',
          'libavcodec/arm/vp8dsp_armv6.S',
        ],
      }],  # (OS == "linux" and target_arch == "arm" and arm_neon == 1) or (OS == "linux" and target_arch == "arm")
      ['(OS == "linux" and ffmpeg_branding == "ChromeOS") or (OS == "linux" and ffmpeg_branding == "ChromiumOS")', {
        'c_sources': [
          'libavcodec/flac.c',
          'libavcodec/flac_parser.c',
          'libavcodec/flacdata.c',
          'libavcodec/flacdec.c',
          'libavcodec/flacdsp.c',
          'libavformat/autorename_libavformat_flacdec.c',
        ],
      }],  # (OS == "linux" and ffmpeg_branding == "ChromeOS") or (OS == "linux" and ffmpeg_branding == "ChromiumOS")
      ['(OS == "android" and target_arch == "arm") or (OS == "linux" and target_arch == "arm" and arm_neon == 1) or (OS == "linux" and target_arch == "arm")', {
        'c_sources': [
          'libavcodec/arm/fft_fixed_init_arm.c',
          'libavcodec/arm/fft_init_arm.c',
          'libavcodec/arm/vorbisdsp_init_arm.c',
          'libavutil/arm/autorename_libavutil_arm_cpu.c',
          'libavutil/arm/float_dsp_init_arm.c',
          'libavutil/arm/float_dsp_init_vfp.c',
        ],
        'asm_sources': [
          'libavcodec/arm/fft_vfp.S',
          'libavcodec/arm/mdct_vfp.S',
          'libavutil/arm/float_dsp_vfp.S',
        ],
      }],  # (OS == "android" and target_arch == "arm") or (OS == "linux" and target_arch == "arm" and arm_neon == 1) or (OS == "linux" and target_arch == "arm")
      ['(OS == "linux" and ffmpeg_branding == "Chrome") or (OS == "linux" and ffmpeg_branding == "ChromeOS") or (OS == "mac" and ffmpeg_branding == "Chrome") or (OS == "win" and ffmpeg_branding == "Chrome")', {
        'c_sources': [
          'libavcodec/cabac.c',
          'libavcodec/h264.c',
          'libavcodec/h264_cabac.c',
          'libavcodec/h264_cavlc.c',
          'libavcodec/h264_direct.c',
          'libavcodec/h264_loopfilter.c',
          'libavcodec/h264_mb.c',
          'libavcodec/h264_parser.c',
          'libavcodec/h264_picture.c',
          'libavcodec/h264_ps.c',
          'libavcodec/h264_refs.c',
          'libavcodec/h264_sei.c',
          'libavcodec/h264_slice.c',
          'libavcodec/h264chroma.c',
          'libavcodec/h264dsp.c',
          'libavcodec/h264idct.c',
          'libavcodec/h264qpel.c',
          'libavcodec/startcode.c',
        ],
      }],  # (OS == "linux" and ffmpeg_branding == "Chrome") or (OS == "linux" and ffmpeg_branding == "ChromeOS") or (OS == "mac" and ffmpeg_branding == "Chrome") or (OS == "win" and ffmpeg_branding == "Chrome")
      ['(OS == "linux" and ffmpeg_branding == "ChromeOS") or (ffmpeg_branding == "Chrome")', {
        'c_sources': [
          'libavcodec/aac_ac3_parser.c',
          'libavcodec/aac_parser.c',
          'libavcodec/aacadtsdec.c',
          'libavcodec/aacps_float.c',
          'libavcodec/aacpsdsp_float.c',
          'libavcodec/aacsbr.c',
          'libavcodec/aactab.c',
          'libavcodec/ac3tab.c',
          'libavcodec/autorename_libavcodec_aacdec.c',
          'libavcodec/autorename_libavcodec_mpegaudiodsp.c',
          'libavcodec/dct.c',
          'libavcodec/dct32_fixed.c',
          'libavcodec/dct32_float.c',
          'libavcodec/imdct15.c',
          'libavcodec/kbdwin.c',
          'libavcodec/mpegaudio.c',
          'libavcodec/mpegaudio_parser.c',
          'libavcodec/mpegaudiodec_fixed.c',
          'libavcodec/mpegaudiodecheader.c',
          'libavcodec/mpegaudiodsp_data.c',
          'libavcodec/mpegaudiodsp_fixed.c',
          'libavcodec/mpegaudiodsp_float.c',
          'libavcodec/sbrdsp.c',
          'libavcodec/sinewin.c',
          'libavcodec/sinewin_fixed.c',
          'libavformat/aacdec.c',
          'libavformat/apetag.c',
          'libavformat/img2.c',
          'libavformat/mov.c',
          'libavformat/mov_chan.c',
          'libavformat/mp3dec.c',
        ],
      }],  # (OS == "linux" and ffmpeg_branding == "ChromeOS") or (ffmpeg_branding == "Chrome")
      ['(OS == "linux" and ffmpeg_branding == "ChromeOS") or (OS == "linux" and ffmpeg_branding == "ChromiumOS") or (ffmpeg_branding == "Chrome")', {
        'c_sources': [
          'libavformat/rawdec.c',
        ],
      }],  # (OS == "linux" and ffmpeg_branding == "ChromeOS") or (OS == "linux" and ffmpeg_branding == "ChromiumOS") or (ffmpeg_branding == "Chrome")
      ['(OS == "linux") or (OS == "mac") or (OS == "win")', {
        'c_sources': [
          'libavcodec/h264pred.c',
          'libavcodec/hpeldsp.c',
          'libavcodec/videodsp.c',
          'libavcodec/vp3.c',
          'libavcodec/vp3_parser.c',
          'libavcodec/vp3dsp.c',
          'libavcodec/vp56rac.c',
          'libavcodec/vp8.c',
          'libavcodec/vp8_parser.c',
          'libavcodec/vp8dsp.c',
        ],
      }],  # (OS == "linux") or (OS == "mac") or (OS == "win")
      ['(1)', {
        'c_sources': [
          'libavcodec/allcodecs.c',
          'libavcodec/autorename_libavcodec_utils.c',
          'libavcodec/avdct.c',
          'libavcodec/avfft.c',
          'libavcodec/avpacket.c',
          'libavcodec/avpicture.c',
          'libavcodec/bitstream.c',
          'libavcodec/bitstream_filter.c',
          'libavcodec/codec_desc.c',
          'libavcodec/dirac.c',
          'libavcodec/dv_profile.c',
          'libavcodec/fft_fixed.c',
          'libavcodec/fft_fixed_32.c',
          'libavcodec/fft_float.c',
          'libavcodec/fft_init_table.c',
          'libavcodec/golomb.c',
          'libavcodec/imgconvert.c',
          'libavcodec/mathtables.c',
          'libavcodec/mdct_fixed.c',
          'libavcodec/mdct_fixed_32.c',
          'libavcodec/mdct_float.c',
          'libavcodec/mpeg12data.c',
          'libavcodec/mpeg4audio.c',
          'libavcodec/mpegaudiodata.c',
          'libavcodec/options.c',
          'libavcodec/opus.c',
          'libavcodec/opus_parser.c',
          'libavcodec/parser.c',
          'libavcodec/pcm.c',
          'libavcodec/pthread.c',
          'libavcodec/pthread_frame.c',
          'libavcodec/pthread_slice.c',
          'libavcodec/qsv_api.c',
          'libavcodec/raw.c',
          'libavcodec/rdft.c',
          'libavcodec/vorbis.c',
          'libavcodec/vorbis_data.c',
          'libavcodec/vorbis_parser.c',
          'libavcodec/vorbisdec.c',
          'libavcodec/vorbisdsp.c',
          'libavcodec/xiph.c',
          'libavformat/allformats.c',
          'libavformat/autorename_libavformat_options.c',
          'libavformat/autorename_libavformat_pcm.c',
          'libavformat/autorename_libavformat_utils.c',
          'libavformat/avio.c',
          'libavformat/aviobuf.c',
          'libavformat/cutils.c',
          'libavformat/dump.c',
          'libavformat/flac_picture.c',
          'libavformat/format.c',
          'libavformat/id3v1.c',
          'libavformat/id3v2.c',
          'libavformat/isom.c',
          'libavformat/matroska.c',
          'libavformat/matroskadec.c',
          'libavformat/metadata.c',
          'libavformat/mux.c',
          'libavformat/oggdec.c',
          'libavformat/oggparsecelt.c',
          'libavformat/oggparsedirac.c',
          'libavformat/oggparseflac.c',
          'libavformat/oggparseogm.c',
          'libavformat/oggparseopus.c',
          'libavformat/oggparseskeleton.c',
          'libavformat/oggparsespeex.c',
          'libavformat/oggparsetheora.c',
          'libavformat/oggparsevorbis.c',
          'libavformat/oggparsevp8.c',
          'libavformat/os_support.c',
          'libavformat/replaygain.c',
          'libavformat/riff.c',
          'libavformat/riffdec.c',
          'libavformat/rmsipr.c',
          'libavformat/url.c',
          'libavformat/vorbiscomment.c',
          'libavformat/wavdec.c',
          'libavutil/aes.c',
          'libavutil/autorename_libavutil_cpu.c',
          'libavutil/avstring.c',
          'libavutil/base64.c',
          'libavutil/bprint.c',
          'libavutil/buffer.c',
          'libavutil/camellia.c',
          'libavutil/channel_layout.c',
          'libavutil/color_utils.c',
          'libavutil/crc.c',
          'libavutil/dict.c',
          'libavutil/display.c',
          'libavutil/downmix_info.c',
          'libavutil/error.c',
          'libavutil/eval.c',
          'libavutil/fifo.c',
          'libavutil/file_open.c',
          'libavutil/fixed_dsp.c',
          'libavutil/float_dsp.c',
          'libavutil/frame.c',
          'libavutil/imgutils.c',
          'libavutil/intmath.c',
          'libavutil/lfg.c',
          'libavutil/log.c',
          'libavutil/log2_tab.c',
          'libavutil/mathematics.c',
          'libavutil/md5.c',
          'libavutil/mem.c',
          'libavutil/opt.c',
          'libavutil/parseutils.c',
          'libavutil/pixdesc.c',
          'libavutil/pixelutils.c',
          'libavutil/random_seed.c',
          'libavutil/rational.c',
          'libavutil/reverse.c',
          'libavutil/samplefmt.c',
          'libavutil/sha.c',
          'libavutil/stereo3d.c',
          'libavutil/tea.c',
          'libavutil/threadmessage.c',
          'libavutil/time.c',
          'libavutil/timecode.c',
          'libavutil/twofish.c',
          'libavutil/utils.c',
        ],
      }],  # (1)
    ],  # conditions
  },
}
